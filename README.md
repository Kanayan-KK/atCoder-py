# AtCoder Python環境

サンプルテストは、既定で`Python (PyPy 3.11-v7.3.20)`を使います。
必要な問題では`Python (CPython 3.13.7)`も選べます。
各問題の解答と公式サンプルを`problems`にまとめています。

## 初回準備

PowerShellで次を実行します。

```powershell
.\scripts\setup.ps1
```

`uv`が既定のCPython環境`.venv`と、選択実行用のPyPy環境`.venv-pypy`を準備します。
CPythonは`3.13.7`、PyPyはAtCoderと同じビルド`7.3.20`です。
NumPyと、開発用の`ruff`、`pyright`は既定のCPython環境へ導入します。

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

CPythonで実行する場合:

```powershell
.\scripts\test-samples.ps1 problems/ABC468/abc468-a -Runtime CPython
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

デバッグ構成は、`.venv-pypy`のPyPyを先頭に表示します。
PyPy構成を選ぶと`.venv-pypy`で実行され、どちらもサンプルが自動入力されます。
VS Codeには推奨拡張のPython、Pylance、Python Debugger、Ruffを入れてください。

## Zed

Zedでは、このリポジトリのルートをフォルダーとして開きます。
初回はコマンドパレットの `task: spawn` から `AtCoder: 初回準備` を実行します。

### タスク

1. コマンドパレットで `task: spawn` を実行します。
2. `AtCoder: サンプルテスト` を選びます。
3. ターミナルで問題ディレクトリを入力します。
4. ターミナルで `CPython` または `PyPy` を入力します。空欄では `PyPy` を使います。

問題ディレクトリは、リポジトリのルートからの相対パスで指定します。
`Main.py` を開いている場合、タスクはその問題ディレクトリを初期値として表示します。
問題ディレクトリの入力で Enter を押すと、タスクは表示した初期値を使います。
タスクは、指定した問題の全サンプルを検証します。
`AtCoder: Ruffチェック` は、プロジェクト全体を検証します。
各タスクは、実行前に編集内容を保存します。

### デバッグ

1. 対象問題の `Main.py` を保存し、停止したい行にブレークポイントを置きます。
2. `F4` を押します。
3. `AtCoder: CPythonでデバッグ` または `AtCoder: PyPyでデバッグ` を選びます。
4. ターミナルで問題ディレクトリとサンプル番号を入力します。

問題ディレクトリは、リポジトリのルートからの相対パスで指定します。
サンプル番号は `01` や `02` と入力します。空欄では `01` を使います。
ランナーは、指定した問題の `samples/<サンプル番号>.in` を標準入力へ接続します。
`Main.py` を開いている場合、ランナーはその問題ディレクトリを初期値として表示します。
問題ディレクトリの入力で Enter を押すと、ランナーは表示した初期値を使います。
別の問題パスを入力すると、ランナーは指定した問題の `Main.py` を実行します。
Zedは、デバッグに必要な `debugpy` を自動で準備します。

Zedでは、問題とサンプルの入力欄をターミナルに表示します。
VS Codeでは、従来どおり専用の入力欄と選択肢を表示します。

設定形式と操作の詳細は、Zed公式の[タスク](https://zed.dev/docs/tasks)と
[Pythonデバッグ](https://zed.dev/docs/languages/python#debugging)を参照してください。

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
