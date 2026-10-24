$ErrorActionPreference = "Stop"

# VS Codeの入力欄に相当する選択をターミナルで受付
$problem = Read-Host "問題ディレクトリ (リポジトリのルートからの相対パス)"
if ([string]::IsNullOrWhiteSpace($problem)) { throw "問題ディレクトリを入力してください。" }
$runtime = Read-Host "実行するPython処理系 (CPython / PyPy) [PyPy]"
if ([string]::IsNullOrWhiteSpace($runtime)) { $runtime = "PyPy" }
if ($runtime -notin @("CPython", "PyPy")) { throw "CPythonまたはPyPyを指定してください。" }

# 既存のサンプルテストに処理を委譲
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
& "$PSScriptRoot/test-samples.ps1" -Problem $problem -Runtime $runtime
exit $LASTEXITCODE
