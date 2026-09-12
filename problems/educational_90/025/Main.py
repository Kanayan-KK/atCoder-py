# 025 - Digit Product Equation（★7）
# 問題画像: 025.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_y
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/025.txt
#
# 【問題】
# 関数 f(x) を次のように定義します。
# ・f(x) = [x の各位の数字の積]
# 例えば、f(777)=343、f(8691)=432、f(869120)=0 です。
#
# 整数 N と B が与えられるので、1 以上 N 以下の整数 m の中で m - f(m) = B
# となるものの個数を求めてください。
#
# 【制約】
# ・1 ≦ N < 10^11
# ・1 ≦ B < 10^11
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N B
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/025
