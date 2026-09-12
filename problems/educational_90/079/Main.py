# 079 - Two by Two（★3）
# 問題画像: 079.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_ca
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/079.txt
#
# 【問題】
# H×W の 2 次元配列 A が与えられます。あなたは以下の 2
# 種類の操作を好きな順番で何度でも行うことが出来ます。
#
# ・整数 x, y (1 ≦ x < H, 1 ≦ y < W) を選び、A[x, y], A[x+1, y], A[x, y+1], A[x+1, y+1]
# の値をそれぞれ 1 ずつ増やす。
# ・整数 x, y (1 ≦ x < H, 1 ≦ y < W) を選び、A[x, y], A[x+1, y], A[x, y+1], A[x+1, y+1]
# の値をそれぞれ 1 ずつ減らす。
#
# 操作を 0 回以上行うことで A を B に一致させることは可能でしょうか。
# もし可能ならば、最小の操作回数も答えてください。
#
# 【制約】
# ・2 ≦ H, W ≦ 100
# ・0 ≦ A[i, j] ≦ 10^5
# ・入力は全て整数
#
# 【入出力形式】
# 入力形式
# H W
# A[1, 1] A[1, 2] ... A[1, W]
# A[2, 1] A[2, 2] ... A[2, W]
# :
# A[H, 1] A[H, 2] ... A[H, W]
# B[1, 1] B[1, 2] ... B[1, W]
# B[2, 1] B[2, 2] ... B[2, W]
# :
# B[H, 1] B[H, 2] ... B[H, W]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/079
