# 041 - Piles in AtCoder Farm（★7）
# 問題画像: 041.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_ao
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/041.txt
#
# 【問題】
# AtCoder 農園には N 個の杭があり、i 個目の杭は座標 (X[i], Y[i]) に打たれています。
#
# あなたはすべての杭を囲む塀を作り、塀の周上または内側にある全ての格子点に杭を打ちたいと思っていま
# す。長い塀を作るのは疲れるので、すべての杭を囲むような塀のうち最も周の長さが短いものを作ります。
#
# あなたが新しく打つ必要がある杭の本数を求めてください。
# ただし、杭の大きさや塀の厚さは無視できるものとします。
#
#
# 【制約】
# ・3 ≦ N ≦ 10^5
# ・0 ≦ X[i], Y[i] ≦ 10^9
# ・(X[i], Y[i]) ≠ (X[j], Y[j]) [i ≠ j]
# ・入力はすべて整数
#
#
# 【小課題】
# 1. (2 点) N = 3, X[i] ≦ 1000, Y[i] ≦ 1000
# 2. (2 点) X[i] ≦ 1000, Y[i] ≦ 1000
# 3. (3 点) 追加の制約はない
#
# 【入出力形式】
# 入力形式
# N
# X[1] Y[1]
# X[2] Y[2]
#  :
# X[N] Y[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/041
