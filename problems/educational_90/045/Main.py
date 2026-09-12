# 045 - Simple Grouping（★6）
# 問題画像: 045.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_as
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/045.txt
#
# 【問題】
# ユークリッド平面上に、N 個の点 (X[1], Y[1]), (X[2], Y[2]), ..., (X[N], Y[N]) があります。
#
# これらを、
#  1) どのグループにも属さない点
#  2) 複数のグループに入る点
#  3) ひとつも点が属さないグループ
# のないように K 個のグループに分けることを考えます。
#
# 同一グループ内での 2 点間距離の最大値を最小化し、その 2 乗の値を出力してください。
#
#
# 【制約】
# ・2 ≦ K ≦ N ≦ 15
# ・0 ≦ X[i], Y[i] ≦ 10^9
# ・(X[i], Y[i]) ≠ (X[j], Y[j])
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N K
# X[1] Y[1]
# X[2] Y[2]
#  :
# X[N] Y[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/045
