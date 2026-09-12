# 066 - Various Arrays（★5）
# 問題画像: 066.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_bn
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/066.txt
#
# 【問題】
# 数列屋の高橋くんは長さ N の数列 A を作っています。数列 A の i 番目の要素 A[i] の値は、L[i] ≦
# A[i] ≦ R[i]
# を満たす整数から一様ランダムに選ぶことで決定されます。
#
# このようにしてできた数列 A の転倒数の期待値を求めてください。
#
# なお、長さが M である数列 X の「転倒数」とは、i < j かつ X[i] > X[j] であるような (i, j) (1 ≦ i,
# j ≦ M) の個数を指します。
#
# 【制約】
# - 1 ≦ N ≦ 100
# - 1 ≦ L[i] ≦ R[i] ≦ 100
# - 入力は全て整数で与えられる
#
# ※絶対誤差または相対誤差 10^{-7} 以下で AC
#
# 【入出力形式】
# 入力形式
# N
# L_1 R_1
# ...
# L_N R_N
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/066
