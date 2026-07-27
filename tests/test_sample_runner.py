import os
import subprocess
import sys
import unittest
from pathlib import Path


class SampleRunnerTest(unittest.TestCase):
    def test_matching_output_passes(self) -> None:
        # 実ファイルと子プロセスでサンプル実行器を検証
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [
                sys.executable,
                str(root / "scripts" / "test_samples.py"),
                str(root / "tests" / "fixtures" / "sample-runner"),
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("判定：OK", result.stdout)

    def test_debug_runner_connects_sample_to_stdin(self) -> None:
        # input()と同じ標準入力経路へサンプルを接続
        root = Path(__file__).resolve().parents[1]
        fixture = root / "tests" / "fixtures" / "sample-runner"
        env = os.environ.copy()
        env["ATCODER_INPUT_FILE"] = str(fixture / "samples" / "01.in")
        result = subprocess.run(
            [
                sys.executable,
                str(root / "scripts" / "debug_problem.py"),
                str(fixture / "Main.py"),
            ],
            capture_output=True,
            text=True,
            check=False,
            env=env,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.strip(), "6")


if __name__ == "__main__":
    unittest.main()
