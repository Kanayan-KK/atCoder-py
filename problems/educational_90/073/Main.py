# 073 - We Need Both a and b（★5）
# 問題画像: 073.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_bu
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/073.txt
#
# 【問題】
# N 頂点の木が与えられます。木の頂点は 1, 2, ⋯ , N と番号付けられており、i 番目の辺は頂点 a_i
# と頂点 b_i を双方向に結んでいます。
# 各頂点には `a`, `b` いずれかの文字が書かれており、頂点 i に書かれている文字は c_i です。
#
# 0 本以上の辺を削除する方法は 2^{N − 1} 通りありますが、その中で「辺を削除した後、すべての連結成
# 分が `a`, `b` 両方の文字を含む」ものは何通りかを求め、10^{9 + 7}
# で割った余りを出力してください。
#
#
# 【制約】
# ・2 ≦ N ≦ 10^5
# ・c_i は `a`, `b` のいずれか
# ・1 ≦ a_i, b_i ≦ N
# ・与えられるグラフは木である
#
# 【入出力形式】
# 入力形式
# N
# c_1 ... c_N
# a_1 b_1
# :
# a_{N-1} b_{N-1}
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/073
