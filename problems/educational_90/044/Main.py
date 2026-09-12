# 044 - Shift and Swapping（★3）
# 問題画像: 044.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_ar
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/044.txt
#
# 【問題】
# 長さが N の整数列 A があります。次の Q 個のクエリを順に処理してください。
# ・T[i] = 1 のとき: 数列 A の x[i] 番目の値と y[i] 番目の値を入れ替える
# ・T[i] = 2 のとき: 数列 A を右方向にひとつシフトする
# ・T[i] = 3 のとき: 数列 A の x[i] 番目の値を出力する
#
# 【制約】
# ・2 ≦ N ≦ 200000
# ・1 ≦ Q ≦ 200000
# ・1 ≦ A_i ≦ 10^9
# ・1 ≦ T[i] ≦ 3
# ・T[i] = 1 のとき 1 ≦ x[i], y[i] ≦ N, x[i] ≠ y[i]
# ・T[i] = 2 のとき x[i] = y[i] = 0
# ・T[i] = 3 のとき 1 ≦ x[i] ≦ N, y[i] = 0
#
# 【入出力形式】
# 入力形式
# N Q
# A[1] A[2] ... A[N]
# T[1] x[1] y[1]
#  :
# T[Q] x[Q] y[Q]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/044
