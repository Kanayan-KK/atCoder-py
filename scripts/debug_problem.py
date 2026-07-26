from __future__ import annotations

import os
import runpy
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("デバッグ対象のMain.pyを指定してください。")

    # 選択したサンプルを対象プログラムの標準入力へ接続
    source_path = Path(sys.argv[1]).resolve()
    input_path = Path(os.environ["ATCODER_INPUT_FILE"]).resolve()
    original_argv = sys.argv
    with input_path.open(encoding="utf-8") as sample:
        sys.stdin = sample
        sys.argv = [str(source_path)]
        runpy.run_path(str(source_path), run_name="__main__")
    sys.argv = original_argv


if __name__ == "__main__":
    main()
