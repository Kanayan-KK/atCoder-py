# 028 - Cluttered Paper（★4）
# 問題画像: 028.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_ab
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/028.txt
#
# 【問題】
# 二次元平面上に N 枚の長方形の紙があります。
# 全ての紙は辺が x 軸または y 軸に平行になるように配置されており、i 枚目の紙の左下角の座標は
# (lx[i], ly[i])、右上角の座標は (rx[i], ry[i]) です。
#
# k = 1, 2, 3, ..., N それぞれについて、次の値を求めてください。
# ・神がちょうど k 枚重なっている部分の面積
#
#
# 【制約】
# ・1 ≦ N ≦ 10^5
# ・0 ≦ lx[i] < rx[i] ≦ 1000
# ・0 ≦ ly[i] < ry[i] ≦ 1000
# ・入力はすべて整数
#
# 【入出力形式】
# 入力形式
# N
# lx[1] ly[1] rx[1] ry[1]
# lx[2] ly[2] rx[2] ry[2]
#  :
# lx[N] ly[N] rx[N] ry[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/028
