# 026 - Independent Set on a Tree（★4）
# 問題画像: 026.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_z
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/026.txt
#
# 【問題】
# N 頂点の木があり、頂点には 1, 2, 3, ..., N と番号が振られています。
# i (1≦i≦N-1) 番目の辺は、頂点 A[i] と B[i] を結んでいます。
#
# 最初、木のすべての頂点は白く塗られています。
# N/2 個の頂点を、次の条件を満たすように赤く塗る方法を 1 つ出力してください。
# ・赤く塗られている 2 つの頂点が隣接している場所は存在しない。ただし、頂点 u, v
# が隣接しているとは、頂点 u と v　を直接結ぶ辺が存在することを指す。
#
# 【制約】
# ・1 ≦ N ≦ 10^5
# ・N は偶数
# ・1 ≦ A[i] < B[i] ≦ N
# ・入力はすべて整数
# ・与えられるグラフは木である
#
# 【入出力形式】
# 入力形式
# N
# A[1] B[1]
# A[2] B[2]
#  :
# A[N-1] B[N-1]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/026
