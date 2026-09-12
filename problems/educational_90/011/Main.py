# 011 - Gravy Jobs（★6）
# 問題画像: 011.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_k
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/011.txt
#
# 【問題】
# ABC 君にお仕事の依頼が N 件来ました。
# 番号 i の仕事が締切が D[i] 日目の終わりであり、連続する C[i] 日間を使わなければ完了できません。
# また、番号 i の仕事を完遂すると S[i] 円の報酬がもらえます。
# また、1 日には高々 1 種類しか仕事を行うことができません。
#
# ABC 君が上手く取り掛かる仕事を選び、スケジュールを組んだ場合、彼が得られる金額として考えられる最
# 大値を求めてください。
#
# 【制約】
# ・1 ≦ N ≦ 5000
# ・1 ≦ C[i], D[i] ≦ 5000
# ・1 ≦ S[i] ≦ 10^9
# ・入力はすべて整数
#
# 【小課題】
# 1. N ≦ 8
# 2. N ≦ 20
# 3. N ≦ 5000
#
# 【入出力形式】
# 入力形式
# N
# D[1] C[1] S[1]
# D[2] C[2] S[2]
#  :
# D[N] C[N] S[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/011
