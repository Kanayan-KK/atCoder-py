# 039 - Tree Distance（★5）
# 問題画像: 039.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_am
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/039.txt
#
# 【問題】
# N 頂点の木が与えられます。木の頂点にはそれぞれ 1 から N までの番号が振られています。
# i 番目の辺は頂点 a[i] と頂点 b[i] を双方向に結んでおり、長さはすべて 1 です。
#
# ---
# dist(1, 2) + dist(1, 3) + dist(1, 4) + ... + dist(1, N) + dist(2, 3) + ...  + dist(2, N) + ... +
# dist(N-2, N-1) + dist(N-2, N) + dist(N-1, N)
# ---
#
# の値を計算してください。ただし、dist(u, v) は頂点 u から v までの最短距離とします。
#
# 【制約】
# ・2 ≦ N ≦ 10^5
# ・1 ≦ a[i], b[i] ≦ N
# ・与えられるグラフは木である
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N
# a[1] b[1]
# a[2] b[2]
#  :
# a[N-1] b[N-1]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/039
