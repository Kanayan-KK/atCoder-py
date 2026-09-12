# 017 - Crossing Segments（★7）
# 問題画像: 017.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_q
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/017.txt
#
# 【問題】
# 円周上に N 個の点があり、時計回りに 1, 2, ..., N と番号付けられています。
# M 個の線分があり、線分 i は点 L[i] と R[i] を結んでいます。
#
# 組 (s, t) [1 ≦ s < t ≦ M] のうち、次の条件を満たすものの個数を出力してください。
# ・線分 s と t が端点以外で交わる。
#
# 【制約】
# ・3 ≦ N ≦ 10^5
# ・3 ≦ M ≦ 10^5
# ・1 ≦ L[i] < R[i] ≦ N
# ・(L[i], R[i]) ≠ (L[j], R[j]) [i ≠ j]
#
# 【小課題】
# 1. N ≦ 1000、M ≦ 1000
# 2. N ≦ 1000
# 3. 追加の制約はない
#
# 【入出力形式】
# 入力形式
# N M
# L[1] R[1]
# L[2] R[2]
#  :
# L[M] R[M]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/017
