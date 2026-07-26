$ErrorActionPreference = "Stop"
$env:UV_PYTHON_PYPY_BUILD = "7.3.20"

# AtCoderと同じPyPyビルドで仮想環境を作成
uv sync
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

# 実際に選択された処理系とバージョンを表示
uv run python -c "import platform, sys; print(platform.python_implementation(), sys.version)"
exit $LASTEXITCODE
