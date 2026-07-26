param(
    [Parameter(Mandatory = $true)]
    [string]$Problem
)

$ErrorActionPreference = "Stop"

# PyPyのUTF-8出力をVS Codeターミナルで正しく表示
chcp 65001 | Out-Null
uv run python scripts/test_samples.py $Problem
exit $LASTEXITCODE
