# 029 - Long Bricks（★5）
# 問題画像: 029.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_ac
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/029.txt
#
# 【問題】
# 左右に W 個のマスが並んだ部分があります。
# 最初、すべての部分について、高さは 0 です。
#
# ここに N 個の高さ 1 のレンガを順に積みます。
# i 番目に積むレンガは、左から L[i] 番目から R[i] 番目のマスをちょうど覆うように置きます。
# このとき、レンガが覆う範囲の中で最も高い水平な面で接着します。
#
# 各レンガについて、上面の高さを求めてください。
#
#
# 【制約】
# ・2 ≦ W ≦ 500000
# ・1 ≦ N ≦ 250000
# ・1 ≦ L[i] ≦ R[i] ≦ W
# ・入力はすべて整数
#
# 【小課題】
# 1. W ≦ 9000，N ≦ 9000
# 2. N ≦ 9000
# 3. 追加の制約はない
#
# 【入出力形式】
# 入力形式
# W N
# l[1] r[1]
# l[2] r[2]
#  :
# l[N] r[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/029
