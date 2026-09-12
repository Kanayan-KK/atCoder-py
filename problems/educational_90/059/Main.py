# 059 - Many Graph Queries（★7）
# 問題画像: 059.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_bg
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/059.txt
#
# 【問題】
# N 頂点 M 辺の有向グラフが与えられます。このグラフにおいて、辺 i (1 ≦ i ≦ M) は頂点 X[i] から
# Y[i] に向かいます。
#
# Q 個の、次の形式のクエリに答えてください。
# ・頂点 A[j] から B[j] まで、辺を向きのとおりに通って移動することは可能か？
#
# 【制約】
# ・2 ≦ N ≦ 100000
# ・1 ≦ M ≦ 100000
# ・1 ≦ Q ≦ 100000
# ・1 ≦ X[i] < Y[i] ≦ N
# ・1 ≦ A[j] < B[j] ≦ N
# ・入力はすべて整数
#
# 【小課題】
# 1. (2 点) N, M, Q ≦ 2000
# 2. (5 点) 追加の制約はない
#
# 【入出力形式】
# 入力形式
# N M Q
# X[1] Y[1]
# X[2] Y[2]
#  :
# X[M] Y[M]
# A[1] B[1]
# A[2] B[2]
#  :
# A[Q] B[Q]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/059
