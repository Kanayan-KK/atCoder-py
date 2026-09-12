# 048 - I will not drop out（★3）
# 問題画像: 048.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_av
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/048.txt
#
# 【問題】
# N 問からなる試験があります。i 番目の問題は満点が A[i] 点、部分点が B[i] 点です。
# ここで、部分点は満点より小さく満点の半分より大きいです。つまり A[i]/2 < B[i] < A[i]
# を満たします。
#
# E869120 君はどの問題についても 1 分かけると部分点を取ることができ、さらに 1
# 分かけると満点を取ることができます。
# 試験時間 K 分間で E869120 君が得られる合計得点の最大値を求めてください。
#
# 【制約】
# ・1 ≦ N ≦ 2 × 10^5
# ・1 ≦ K ≦ 2N
# ・3 ≦ A[i] ≦ 10^9
# ・A[i]/2 < B[i] < A[i]
# ・入力は全て整数
#
# 【入出力形式】
# 入力形式
# N K
# A[1] B[1]
# A[2] B[2]
#  :
# A[N] B[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/048
