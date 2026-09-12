# 088 - Similar but Different Ways（★6）
# 問題画像: 088.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_cj
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/088.txt
#
# 【問題】
# N枚のカードがあり、i枚目のカードには正整数A[i]が書かれています。
# E869120とsquareは、これらのカードからそれぞれ1枚以上のカードを選びました。
# 両者のカードの選び方について、次のことが分かっています。
# ・両者が選んだカードに書かれた数の総和は等しかった
# ・両者とも、i=1,2,...,Qに対し、X[i]枚目のカードとY[i]枚目のカードのうち少なくとも一方は選ばなか
# った
# ・両者が選んだカードの集合は等しくなかった
#
# 両者のカードの選び方としてあり得るものを一つ出力してください。
#
# 【制約】
# ・2≦N≦88
# ・0≦Q≦88
# ・1≦A[i]
# ・A[1]+A[2]+...+A[N]≦8888
# ・1≦X[i]<Y[i]≦N
# ・i≠jならば(X[i],Y[i])≠(X[j],Y[j])
# ・入力はすべて整数
# ・条件を満たすカードの選び方が存在する
#
# 【入出力形式】
# 入力形式
# N Q
# A[1] Q[2] ... A[N]
# X[1] Y[1]
# X[2] Y[2]
# :
# X[Q] Y[Q]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/088
