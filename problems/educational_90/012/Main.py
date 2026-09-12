# 012 - Red Painting（★4）
# 問題画像: 012.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_l
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/012.txt
#
# 【問題】
# H 行 W 列のマス目があり、上から i 行目・左から j 列目のマスを (i, j) と表します。
# 最初すべてのマスは白いです。次の Q 個のクエリを順に処理してください。
#
# 《type[i] = 1 のとき》
# ・整数 x, y が与えられる
# ・元々白かったマス (x, y) が赤く塗られる
#
# 《type[i] = 2 のとき》
# ・整数 xa, ya, xb, yb が与えられる
# ・マス (xa, ya) からマス (xb, yb) まで上下左右に隣り合うマスを介して移動し、赤マスのみを通って辿
# り着ける場合は "Yes"、そうでなければ "No" と出力する。
#
# 【制約】
# ・1 ≦ H, W ≦ 2000
# ・1 ≦ Q ≦ 100000
# ・1 ≦ type[i] ≦ 2
# ・type[i] = 1 のとき、1 ≦ x ≦ H、1 ≦ y ≦ W
# ・type[i] = 2 のとき、1 ≦ xa, xb ≦ H、1 ≦ ya, yb ≦ W
#
# 【入出力形式】
# 入力形式
# H W
# Q
# (1 個目のクエリ)
# (2 個目のクエリ)
#  :
# (Q 個目のクエリ)
#
# クエリについて
# T[i] = 1 の場合
# > 1 x y
# T[i] = 2 の場合
# > 2 xa ya xb yb
# といった形で入力が与えられます。
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/012
