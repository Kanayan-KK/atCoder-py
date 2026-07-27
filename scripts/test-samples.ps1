param(
    [Parameter(Mandatory = $true)]
    [string]$Problem,

    [ValidateSet("CPython", "PyPy")]
    [string]$Runtime = "CPython"
)

$ErrorActionPreference = "Stop"

# WindowsのVS Codeターミナルに合わせて両処理系の出力を統一
$env:PYTHONIOENCODING = "cp932"

# 選択した処理系の実行ファイル
$python = if ($Runtime -eq "PyPy") {
    ".\.venv-pypy\Scripts\python.exe"
} else {
    ".\.venv\Scripts\python.exe"
}

# 選択した処理系で結果を表示
& $python scripts/test_samples.py $Problem
exit $LASTEXITCODE
