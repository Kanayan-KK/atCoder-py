from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path


def normalize(value: str) -> str:
    return value.rstrip().replace("\r\n", "\n")


def get_peak_memory_kib(process: subprocess.Popen[str]) -> int | None:
    if sys.platform == "win32":
        import ctypes
        from ctypes import wintypes

        class ProcessMemoryCounters(ctypes.Structure):
            _fields_ = [
                ("cb", wintypes.DWORD),
                ("page_fault_count", wintypes.DWORD),
                ("peak_working_set_size", ctypes.c_size_t),
                ("working_set_size", ctypes.c_size_t),
                ("quota_peak_paged_pool_usage", ctypes.c_size_t),
                ("quota_paged_pool_usage", ctypes.c_size_t),
                ("quota_peak_non_paged_pool_usage", ctypes.c_size_t),
                ("quota_non_paged_pool_usage", ctypes.c_size_t),
                ("pagefile_usage", ctypes.c_size_t),
                ("peak_pagefile_usage", ctypes.c_size_t),
            ]

        # 終了後もPopenが保持するプロセスハンドルからピーク値を取得
        counters = ProcessMemoryCounters()
        counters.cb = ctypes.sizeof(counters)
        get_process_memory_info = ctypes.WinDLL("psapi").GetProcessMemoryInfo
        get_process_memory_info.argtypes = [
            wintypes.HANDLE,
            ctypes.POINTER(ProcessMemoryCounters),
            wintypes.DWORD,
        ]
        get_process_memory_info.restype = wintypes.BOOL
        if not get_process_memory_info(process._handle, ctypes.byref(counters), counters.cb):
            return None
        return round(counters.peak_working_set_size / 1024)

    # Unix系では終了した子プロセスの最大常駐メモリを取得
    import resource

    peak_memory = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    if sys.platform == "darwin":
        peak_memory /= 1024
    return round(peak_memory)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/test_samples.py problems/ABC468/abc468-a")
        return 1

    # 対象問題とサンプルの存在確認
    problem_dir = Path(sys.argv[1]).resolve()
    source_path = problem_dir / "Main.py"
    samples_dir = problem_dir / "samples"
    if not source_path.is_file() or not samples_dir.is_dir():
        print(f"{sys.argv[1]} does not contain Main.py and samples.")
        return 1

    input_paths = sorted(samples_dir.glob("*.in"))
    if not input_paths:
        print(f"{sys.argv[1]}/samples does not contain .in files.")
        return 1

    for input_path in input_paths:
        # 同じ番号の入出力ファイルを組にして実行
        output_path = input_path.with_suffix(".out")
        if not output_path.is_file():
            print(f"Missing: {output_path}")
            return 1

        input_text = input_path.read_text(encoding="utf-8")
        started_at = time.perf_counter()
        process = subprocess.Popen(
            [sys.executable, str(source_path)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding=sys.stdout.encoding,
        )
        stdout, stderr = process.communicate(input=input_text)
        elapsed_ms = (time.perf_counter() - started_at) * 1000
        peak_memory_kib = get_peak_memory_kib(process)
        actual = normalize(stdout)
        expected = normalize(output_path.read_text(encoding="utf-8"))

        # 実行結果と期待値をケースごとに表示
        # 実際の出力と判定を続けて表示
        if input_path != input_paths[0]:
            print()
        print("出力：")
        print(actual or "（出力なし）")
        print(f"実行時間：{elapsed_ms:.3f} ms")
        memory_text = f"{peak_memory_kib} KiB" if peak_memory_kib is not None else "計測不可"
        print(f"使用メモリ：{memory_text}")
        if process.returncode != 0:
            print("判定：NG")
            print(f"実行時エラー：\n{stderr}")
            return 1
        if actual != expected:
            print("判定：NG")
            print(f"期待値：\n{expected}")
            return 1
        print("判定：OK")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
