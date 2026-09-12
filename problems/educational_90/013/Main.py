# 013 - Passing（★5）
# 問題画像: 013.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_m
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/013.txt
#
# 【問題】
# AGC 王国には N 個の交差点があり、それぞれ 1, 2, 3, ..., N と番号付けられています。
# また M 本の道路があり、道路 i は交差点 A[i] と交差点 B[i]
# を双方向に結び、交差点間の移動にかかる時間は C[i] 秒です。
#
# 今日から数えて i (1≦i≦N) 日目には交差点 i でイベントが開催されるため、移動の際には交差点 i
# を経由しなければなりません、
# i = 1, 2, 3, ..., N それぞれについて、i 日目に交差点 1 から交差点 N
# まで移動するのにかかる時間の最小値を求めてください。
#
# 【制約】
# ・2 ≦ N ≦ 100000　←　こっちが正しいです！
# ・1 ≦ M ≦ 100000
# ・1 ≦ A[i] < B[i] ≦ N
# ・(A[i], B[i]) ≠ (A[j], B[j]) [i ≠ j]
# ・1 ≦ C[i] ≦ 10000
# ・いくつかの道路を通って、都市 1 から都市 N までたどり着ける
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N M
# A[1] B[1] C[1]
# A[2] B[2] C[2]
#  :
# A[M] B[M] C[M]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/013
