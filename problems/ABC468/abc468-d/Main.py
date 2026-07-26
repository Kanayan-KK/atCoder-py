import os
import sys
from pathlib import Path


def main() -> None:
    # F5デバッグ時は指定サンプル、それ以外は標準入力を読み取る
    input_file = os.getenv("ATCODER_INPUT_FILE")
    source = Path(input_file).read_text(encoding="utf-8") if input_file else sys.stdin.read()
    values = source.split()

    # ここに解答を実装する
    _ = values


if __name__ == "__main__":
    main()
