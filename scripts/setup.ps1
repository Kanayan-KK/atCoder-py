$ErrorActionPreference = "Stop"
$env:UV_PYTHON_PYPY_BUILD = "7.3.20"

# 既定のCPython環境と開発ツールを作成
uv sync --python "cpython@3.13.7"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

# 選択実行用のPyPy環境を別に作成
uv venv --clear --python "pypy@3.11" .venv-pypy
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

# 実際に用意された両処理系のバージョンを表示
& ".\.venv\Scripts\python.exe" -c "import platform, sys; print('Default:', platform.python_implementation(), sys.version)"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& ".\.venv-pypy\Scripts\python.exe" -c "import platform, sys; print('Optional:', platform.python_implementation(), sys.version)"
exit $LASTEXITCODE
