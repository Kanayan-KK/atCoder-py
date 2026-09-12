# 081 - Friendly Group（★5）
# 問題画像: 081.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_cc
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/081.txt
#
# 【問題】
# 典型高校には N 人の生徒がおり、各生徒には 1 から N までの番号が付けられています。生徒 i の身長は
# A[i]、体重は B[i] です。
#
# N 人の生徒から 1 人以上を選び、次の条件をすべて満たすようにチームを作ります。
#
# ・チーム内のどの 2 人も、身長の差の絶対値が K 以下である
# ・チーム内のどの 2 人も、体重の差の絶対値が K 以下である
#
# チームの人数としてありうる最大の値を求めてください。
#
# 【制約】
# ・1 ≦ N ≦ 2 × 10^5
# ・1 ≦ K ≦ 5000
# ・1 ≦ A[i], B[i] ≦ 5000
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N K
# A[1] B[1]
# A[2] B[2]
#  :
# A[N] B[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/081
