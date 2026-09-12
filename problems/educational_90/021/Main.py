# 021 - Come Back in One Piece（★5）
# 問題画像: 021.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_u
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/021.txt
#
# 【問題】
# N 頂点 M 辺の有向グラフがあります。
# 辺には 1, 2, ..., M と番号が付けられており、辺 i は頂点 A[i] から頂点 B[i] に向かいます。
#
# 次の条件を満たす 2 頂点 (x, y) [1 ≦ x < y ≦ M] の組はいくつありますか。
# ・頂点 x から頂点 y に向かうパス、頂点 y から頂点 x に向かうパス両方が存在する。
#
# 【制約】
# ・2 ≦ N ≦ 100000
# ・1 ≦ M ≦ 200000
# ・1 ≦ A[i], B[i] ≦ M
# ・A[i] ≠ B[i]
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N M
# A[1] B[1]
# A[2] B[2]
#  :
# A[M] B[M]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/021
