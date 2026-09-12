# 009 - Three Point Angle（★6）
# 問題画像: 009.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_i
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/009.txt
#
# 【問題】
# 二次元平面上に N 個の点が存在し、点 i は座標 (X_i, Y_i) にあります。
# あなたは相異なる 3 つの整数 A, B, C (1 ≦ A, B, C ≦ N) を選び、角 ABC (点 A → 点 B → 点 C
# の折れ線で構成される角) の大きさを最大にしたいです。
# そのときの角の大きさを 0 ～ 180 度の範囲で表される度数法で出力してください。
#
# 【制約】
# ・3 ≦ N ≦ 2000
# ・0 ≦ X[i], Y[i] ≦ 10^9
# ・(X[i], Y[i]) ≠ (X[j], Y[j])
# ・入力はすべて整数
# ・絶対誤差または相対誤差が 10^{-8} 以内であれば正解とみなされる
#
# 【入出力形式】
# 入力形式
# N
# X[1] Y[1]
# X[2] Y[2]
# X[3] Y[3]
#  :
# X[N] Y[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/009
