# 036 - Max Manhattan Distance（★5）
# 問題画像: 036.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_aj
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/036.txt
#
# 【問題】
# 二次元座標平面上に相異なる N 個の点 P[1], P[2], ..., P[N] があり、点 P[i] の座標は (x[i], y[i])
# です。
#
# 以下の Q 個のクエリを順に処理してください。
# ・i (1 ≦ i ≦ Q) 番目のクエリでは、整数 q[i] が与えられるので、点 P[q[i]] と N
# 個の点の間のマンハッタン距離の最大値を出力する。
# ・つまり、点 P[s] と P[t] のマンハッタン距離を dist(P[s], P[t]) とするとき、max⁡(dist(P[q[i]],
# P[1]), dist(P[q[i]],
# P[2]), …, dist(P[q[i]], P[N])) の値を出力する。
#
#
# 【制約】
# ・2 ≦ N ≦ 100000
# ・1 ≦ Q ≦ 100000
# ・|x[i]|, |y[i]| ≦ 10^9
# ・(x[i], y[i]) ≠ (x[j], y[j]) [i ≠ j]
# ・1 ≦ q[i] ≦ N
# ・q[i] ≠ q[j] (i ≠ j)
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N Q
# x[1] y[1]
# x[2] y[2]
#  :
# x[N] y[N]
# q[1]
# q[2]
#  :
# q[Q]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/036
