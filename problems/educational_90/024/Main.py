# 024 - Select +／- One（★2）
# 問題画像: 024.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_x
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/024.txt
#
# 【問題】
# 長さ N の正整数列 A = (A[1], A[2], ..., A[N]) および B = (B[1], B[2], ..., B[N])
# が与えられます。
# 次の操作をちょうど K 回行うことで A を B に一致させることができるか判定してください。
# 操作：1 ≦ i ≦ N を満たす i をひとつ選び、A[i] を A[i]-1 または A[i]+1 に置き換える
#
# 【制約】
# ・1 ≦ N ≦ 1000
# ・1 ≦ K ≦ 10^9
# ・1 ≦ A[i], B[i] ≦ 10^6
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N K
# A[1] A[2] ... A[N]
# B[1] B[2] ... B[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/024
