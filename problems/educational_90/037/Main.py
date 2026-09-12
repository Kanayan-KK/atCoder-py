# 037 - Don't Leave the Spice（★5）
# 問題画像: 037.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_ak
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/037.txt
#
# 【問題】
# 香辛料を使う料理が N 個あり、1 から N までの番号が付いています。
# 料理 i (1 ≦ i ≦ N) の価値は V[i] で、作るときに香辛料を消費します。消費する香辛料の量は L[i]
# [mg] 以上 R[i] [mg] 以下の範囲で調節できます。
#
# 以下のことが実現可能かどうか判定し、可能な場合は作る料理の価値の合計としてあり得る最大の値を出力
# してください。
# ・N 種類の料理から何種類か選んで 1 つずつ作ることで、香辛料をちょうど W [mg] 消費する。
# ただし、上で述べた手段以外で香辛料を使うことはできません。
#
#
# 【制約】
# ・1 ≦ W ≦ 10^4
# ・1 ≦ N ≦ 500
# ・1 ≦ L[i] ≦ R[i] ≦W
# ・1 ≦ V[i] ≦ 10^9
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# W N
# L[1] R[1] V[1]
# L[2] R[2] V[2]
#  :
# L[N] R[N] V[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/037
