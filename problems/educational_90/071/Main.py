# 071 - Fuzzy Priority（★7）
# 問題画像: 071.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_bs
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/071.txt
#
# 【問題】
# (1, 2, 3, ... , N) の順列 P = P[1], P[2], P[3], ... , P[N]) であって、以下の条件を満たすものを K
# 個求めてください。 K
# 個存在しない場合は、そのことを報告してください。
#
# ・i = 1, 2, 3, ... , M について、順列 P の中で A[i] は B[i] よりも前にある。
#
# 【制約】
# ・1 ≦ N ≦ 10^5
# ・1 ≦ M ≦ 10^5
# ・1 ≦ K ≦ 10
# ・1 ≦ A[i] ≦ N
# ・1 ≦ B[i] ≦ N
# ・A[i] ≠ B[i]
# ・i ≠ j ならば (A[i], B[i]) ≠ (A[j], B[j])
# ・入力はすべて整数
#
# 【小課題】
# 1. (2 点) N ≦ 10^3
# 2. (3 点) K = 1
# 3. (2 点) 追加の制約はない
#
# 【入出力形式】
# 入力形式
# N M K
# A[1] B[1]
# A[2] B[2]
# A[3] B[3]
#  :
# A[M] B[M]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/071
