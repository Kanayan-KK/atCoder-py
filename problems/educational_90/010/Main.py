# 010 - Score Sum Queries（★2）
# 問題画像: 010.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_j
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/010.txt
#
# 【問題】
# ABC 大学には N 人の一年生が在籍しています。
# クラスは 2 つあり、学籍番号 i 番の生徒のクラスは C[i] 組です。
# 今日は期末試験が返却され、学籍番号 i 番の生徒の点数は P[i] 点でした。
#
# 以下の形式の質問が Q 個与えられるので、答えてください。
# ・学籍番号 L[i] ～ R[i] の 1 組生徒における、期末試験点数の合計
# ・学籍番号 L[i] ～ R[i] の 2 組生徒における、期末試験点数の合計
# ・これら 2 つをそれぞれ求めよ。
#
# 【制約】
# ・1 ≦ N ≦ 10^5
# ・1 ≦ C[i] ≦ 2
# ・0 ≦ P[i] ≦ 100
# ・1 ≦ Q ≦ 10^5
# ・1 ≦ L[i] ≦ R[i] ≦ N
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N
# C[1] P[1]
# C[2] P[2]
#  :
# C[N] P[N]
# Q
# L[1] R[1]
# L[2] R[2]
#  :
# L[Q] R[Q]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/010
