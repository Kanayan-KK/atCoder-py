# 004 - Cross Sum（★2）
# 問題画像: 004.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_d
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/004.txt
#
# 【問題】
# H 行 W 列のマス目があります。上から i (1 ≦ i ≦ H) 行目、左から j (1 ≦ j ≦ W) 列目にあるマス (i,
# j) には、整数 A[i][j] が書かれています。
#
# すべてのマス (i, j) [1 ≦ i ≦ H, 1 ≦ j ≦ W] について、以下の値を求めてください。
# ・マス (i, j) と同じ行または同じ列にあるマス（自分自身を含む）に書かれている整数をすべて合計した
# 値
#
# 【制約】
# ・1 ≦ H ≦ 2000
# ・1 ≦ W ≦ 2000
# ・1 ≦ A[i][j] ≦ 99
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# H W
# A[1][1] A[1][2] ... A[1][W]
# A[2][1] A[2][2] ... A[2][W]
#  :
# A[H][1] A[H][2] ... A[H][W]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/004
