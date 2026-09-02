# AtCoder Python環境

AtCoderの`Python (CPython 3.13.7)`を既定にした作業環境です。
必要な問題では`Python (PyPy 3.11-v7.3.20)`も選べます。
各問題の解答と公式サンプルを`problems`にまとめています。

## 初回準備

PowerShellで次を実行します。

```powershell
.\scripts\setup.ps1
```

`uv`が既定のCPython環境`.venv`と、選択実行用のPyPy環境`.venv-pypy`を準備します。
CPythonは`3.13.7`、PyPyはAtCoderと同じビルド`7.3.20`です。
NumPyと、開発用の`ruff`、`pyright`は既定のCPython環境へ導入します。

## チートシートを追加する

Pythonのチートシートは`cheatsheet`に追加します。
追加・変更後は、対象ファイルの実行、Ruff、Pyright、空白エラーを確認します。
NumPyの基本操作は`cheatsheet/numpy_operations.py`で確認できます。

例として`cheatsheet/dfs.py`を検証する場合:

```powershell
& .\.venv\Scripts\python.exe cheatsheet/dfs.py
& .\.venv\Scripts\ruff.exe check cheatsheet/dfs.py
& .\.venv\Scripts\pyright.exe cheatsheet/dfs.py
git diff --check -- cheatsheet/dfs.py
```

VS CodeのPylanceによる型診断は、CLIでは基盤となるPyrightで検証します。

## ABC468を解く

例としてA問題は`problems/ABC468/abc468-a/Main.py`を編集します。
問題文は各問題ディレクトリの`README.md`から開けます。

全PythonファイルのRuffチェック:

```powershell
uv run ruff check .
```

A問題のサンプルテスト:

```powershell
.\scripts\test-samples.ps1 problems/ABC468/abc468-a
```

PyPyで実行する場合:

```powershell
.\scripts\test-samples.ps1 problems/ABC468/abc468-a -Runtime PyPy
```

解答前の空テンプレートは出力しないため、サンプルテストは`NG`になります。
解答を書いた後に実行してください。

サンプルテスト機能自体のテスト:

```powershell
uv run python -m unittest
```

## VS Code

`Ctrl+Shift+B`で全PythonファイルをRuffチェックできます。
「タスクの実行」から初回準備とサンプルテストも選べます。

### F5デバッグ

1. デバッグする問題の`Main.py`にブレークポイントを置く
2. `F5`を押す
3. CPythonまたはPyPyのデバッグ構成を選ぶ
4. 問題ディレクトリとサンプル番号を入力する

既定は`.venv`のCPythonです。
PyPy構成を選ぶと`.venv-pypy`で実行され、どちらもサンプルが自動入力されます。
VS Codeには推奨拡張のPython、Pylance、Python Debugger、Ruffを入れてください。

## 新しい問題を追加する

```text
problems/
└─ CONTEST/
   └─ contest-task/
      ├─ Main.py
      ├─ README.md
      └─ samples/
         ├─ 01.in
         └─ 01.out
```

`templates/Main.py`を新しい問題ディレクトリへコピーします。
AtCoderへは対象問題の`Main.py`の内容だけを提出します。

## 入力とサンプル比較

`Main.py`は通常どおり標準入力を読みます。
F5デバッグ時はデバッグ専用ランナーが指定サンプルを標準入力へ接続します。
提出コードへデバッグ専用処理を入れる必要はありません。

サンプルテストは行末の空白と改行コードを正規化して文字列比較します。
正解が複数ある問題では、正しい別解でもサンプル出力と異なると失敗します。
