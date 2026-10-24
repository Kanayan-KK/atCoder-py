from __future__ import annotations

import os
import runpy
import sys
from pathlib import Path


def main() -> None:
    # Zedではターミナルで問題とサンプルを選択
    interactive = sys.argv[1:] == ["--interactive"]
    if interactive:
        root = Path(__file__).resolve().parents[1]
        problem = input("問題ディレクトリ (リポジトリのルートからの相対パス): ").strip()
        if not problem:
            raise SystemExit("問題ディレクトリを入力してください。")
        sample_number = input("サンプル番号 [01]: ").strip() or "01"
        source_path = (root / problem / "Main.py").resolve()
        input_path = source_path.parent / "samples" / f"{sample_number}.in"
    elif len(sys.argv) == 2:
        source_path = Path(sys.argv[1]).resolve()
        input_path = Path(os.environ["ATCODER_INPUT_FILE"]).resolve()
    else:
        raise SystemExit("デバッグ対象のMain.pyを指定してください。")

    # 選択したサンプルを対象プログラムの標準入力へ接続
    if not source_path.is_file():
        raise SystemExit(f"解答ファイルがありません: {source_path}")
    if not input_path.is_file():
        raise SystemExit(f"入力ファイルがありません: {input_path}")
    if interactive:
        os.chdir(source_path.parent)
    original_argv = sys.argv
    with input_path.open(encoding="utf-8") as sample:
        sys.stdin = sample
        sys.argv = [str(source_path)]
        runpy.run_path(str(source_path), run_name="__main__")
    sys.argv = original_argv


if __name__ == "__main__":
    main()
