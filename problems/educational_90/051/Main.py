# 051 - Typical Shop（★5）
# 問題画像: 051.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_ay
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/051.txt
#
# 【問題】
# 典型商店には N 個の区別できる品物があります。i 番目の品物 i の値段は A[i] 円です。
# あなたは商店に売られている品物からちょうど K 個を選んで、選んだ値段の合計が P
# 円以下となるように買い物をしたいです。あり得る品物の選び方は何通りあるでしょうか？
# なお、2 通りの品物の選び方は、ある品物 i があって、品物 i
# が一方では選ばれており他方では選ばれていないときに区別されます。
#
# 【制約】
# ・1 ≦ K ≦ N ≦ 40
# ・1 ≦ P ≦ 10^{18}
# ・1 ≦ A[i] ≦ 10^{16}
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N K P
# A[1] A[2] A[3] ... A[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/051
