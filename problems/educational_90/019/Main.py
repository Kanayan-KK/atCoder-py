# 019 - Pick Two（★6）
# 問題画像: 019.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_s
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/019.txt
#
# 【問題】
# 2N 人が一列に並んでおり、左から i 番目の人の身長は A[i] です。
#
# YouTuber である ABC 君はこれからライブショーを行います。ショーでは、以下の操作を N 回行います。
# ・隣り合う 2 人を選び、列から抜けさせる。一度列から抜けると、もう列に戻ってくることはない。
# ・このとき、あまりにも 2 人の身長差が大きいと視聴者が引いてしまう。具体的には、2 人の身長を x, y
# とするとき、低評価が |x-y| 個付く。
#
# 彼は低評価の個数を最小化したいです。
# 最適にショーを行ったとき、低評価の個数として考えられる最小の値はいくつでしょうか？
#
# 【制約】
# ・1 ≦ N ≦ 200
# ・1 ≦ A[i] ≦ 1000000
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N
# A[1] A[2] ... A[2N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/019
