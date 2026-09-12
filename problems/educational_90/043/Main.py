# 043 - Maze Challenge with Lack of Sleep（★4）
# 問題画像: 043.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_aq
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/043.txt
#
# 【問題】
# 縦 H マス、横 W マスのグリッド状の迷路があり、上から i 行目・左から j 列目のマスを (i,j)
# とします。マス (i,j) は S[i][j] = '#'
# のとき壁で、S[i][j] = '.' のとき壁ではありません。
#
# あなたは上下左右に隣接する壁でないマスへの移動を繰り返してマス (rs,cs) からマス (rt, ct)
# に移動したいです。ただし、移動する方向が変わる回数が多いと脳が疲れてしまうため好ましくありません
# 。また、迷路の外へ出るような移動は許されません。
#
# 移動する方向が変わる回数の最小値を求めてください。
#
# 【制約】
# ・2 ≦ H, W ≦ 1000
# ・1 ≦ rs, rt ≦ H
# ・1 ≦ cs, ct ≦ W
# ・(rs, cs) ≠ (rt, ct)
# ・H, W, rs, cs, rt, ctは整数
# ・S[i][j] は '#' または '.'
# ・S[rs][cs], S[rt][ct] は '.'
# ・マス (rs,cs) からマス (rt,ct) への移動が可能
#
# 【入出力形式】
# 入力形式
# H W
# rs cs
# rt ct
# C[1][1] ... C[1][W]
#  :
# C[H][1] ... C[H][W]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/043
