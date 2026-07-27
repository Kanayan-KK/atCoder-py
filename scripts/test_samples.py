from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def normalize(value: str) -> str:
    return value.rstrip().replace("\r\n", "\n")


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

        result = subprocess.run(
            [sys.executable, str(source_path)],
            input=input_path.read_text(encoding="utf-8"),
            capture_output=True,
            text=True,
            encoding=sys.stdout.encoding,
            check=False,
        )
        actual = normalize(result.stdout)
        expected = normalize(output_path.read_text(encoding="utf-8"))

        # 実行結果と期待値をケースごとに表示
        # 実際の出力と判定を続けて表示
        if input_path != input_paths[0]:
            print()
        print("出力：")
        print(actual or "（出力なし）")
        if result.returncode != 0:
            print("判定：NG")
            print(f"実行時エラー：\n{result.stderr}")
            return 1
        if actual != expected:
            print("判定：NG")
            print(f"期待値：\n{expected}")
            return 1
        print("判定：OK")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
