param(
    [string]$ActiveFile = ""
)

$ErrorActionPreference = "Stop"

# 開いているMain.pyの親ディレクトリを初期値として表示
$defaultProblem = ""
if ($ActiveFile -and (Test-Path -LiteralPath $ActiveFile -PathType Leaf)) {
    if ((Split-Path -Leaf $ActiveFile) -eq "Main.py") {
        $defaultProblem = Split-Path -Parent $ActiveFile
    }
}
$defaultLabel = if ($defaultProblem) { " [$defaultProblem]" } else { "" }

# VS Codeの入力欄に相当する選択をターミナルで受付
$problem = Read-Host "問題ディレクトリ (リポジトリのルートからの相対パス)$defaultLabel"
if ([string]::IsNullOrWhiteSpace($problem)) { $problem = $defaultProblem }
if ([string]::IsNullOrWhiteSpace($problem)) { throw "問題ディレクトリを入力してください。" }
$runtime = Read-Host "実行するPython処理系 (CPython / PyPy) [PyPy]"
if ([string]::IsNullOrWhiteSpace($runtime)) { $runtime = "PyPy" }
if ($runtime -notin @("CPython", "PyPy")) { throw "CPythonまたはPyPyを指定してください。" }

# 既存のサンプルテストに処理を委譲
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
& "$PSScriptRoot/test-samples.ps1" -Problem $problem -Runtime $runtime
exit $LASTEXITCODE
