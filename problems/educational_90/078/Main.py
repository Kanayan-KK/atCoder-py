# 078 - Easy Graph Problem（★2）
# 問題画像: 078.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_bz
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/078.txt
#
# 【問題】
# N 頂点 M 辺の連結な単純無向グラフが与えられます。グラフの頂点には、それぞれ 1 から N
# までの番号が振られています。i 番目の辺は、頂点 a[i] と b[i]
# を双方向に結んでいます。
#
# 以下の条件を満たす頂点の個数はいくつあるか出力してください。
# ・自分自身より頂点番号が小さい隣接頂点がちょうど 1 つ存在する
#
# 【制約】
# ・2 ≦ N ≦ 10^5
# ・N-1 ≦ M ≦ min(N(N-1)/2, 10^5)
# ・1 ≦ a[i], b[i] ≦ N
# ・与えられるグラフは単純
# ・与えられるグラフは連結
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N M
# a[1] b[1]
# :
# a[M] b[M]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/078
