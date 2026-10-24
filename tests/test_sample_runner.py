import os
import subprocess
import sys
import tempfile
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
        self.assertRegex(result.stdout, r"実行時間：\d+\.\d{3} ms")
        self.assertRegex(result.stdout, r"使用メモリ：\d+ KiB")

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

    def test_interactive_debug_selects_problem_and_sample(self) -> None:
        root = Path(__file__).resolve().parents[1]
        # 空白を含む問題パスと既定以外のサンプルを実ファイルで検証
        with tempfile.TemporaryDirectory(prefix="zed problem ") as directory:
            problem = Path(directory)
            (problem / "samples").mkdir()
            (problem / "samples" / "02.in").write_text("selected\n", encoding="utf-8")
            (problem / "marker.txt").write_text("working directory", encoding="utf-8")
            (problem / "Main.py").write_text(
                "from pathlib import Path\n"
                "print(input())\n"
                "print(Path('marker.txt').read_text())\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(root / "scripts" / "debug_problem.py"), "--interactive"],
                cwd=root / "tests",
                input=f"{problem}\n02\n",
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("selected\nworking directory", result.stdout)

    def test_interactive_debug_defaults_to_first_sample(self) -> None:
        root = Path(__file__).resolve().parents[1]
        # 開いているファイルに依存せず、ルートからの相対パスと空欄の番号を解決
        result = subprocess.run(
            [sys.executable, str(root / "scripts" / "debug_problem.py"), "--interactive"],
            cwd=root / "tests",
            input="tests/fixtures/sample-runner\n\n",
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(result.stdout.rstrip().endswith("6"), result.stdout)


if __name__ == "__main__":
    unittest.main()
