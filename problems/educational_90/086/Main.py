# 086 - Snuke's Favorite Arrays（★5）
# 問題画像: 086.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_ch
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/086.txt
#
# 【問題】
# すぬけ君は、以下の 2 つの条件両方を満たす、長さ N の数列 A = (A[1], A[2], ..., A[N])
# が好きです。
#
# > 条件 1｜すべての i (1≦i≦Q) について A[X[i]] OR A[Y[i]] OR A[Z[i]] = W[i] を満たす
# > 条件 2｜すべての j (1≦j≦N) について 0 ≦ A[j] < 2^{60} を満たす
#
# すぬけ君が好きな数列 A の個数を 10^9+7 で割った余りを求めてください。
# ※ただし OR はビットごとの論理和です
#
# 【制約】
# - 3 ≦ N ≦ 12
# - 1 ≦ Q ≦ 50
# - 1 ≦ x[i] < y[i] < z[i] ≦ N
# - 0 ≦ w_i < 2^{60}
# - 入力は全て整数で与えられる
#
# 【入出力形式】
# 入力形式
# N Q
# x_1 y_1 z_1 w_1
# ...
# x_Q y_Q z_Q w_Q
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/086
