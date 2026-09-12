# 074 - ABC String 2（★6）
# 問題画像: 074.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_bv
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/074.txt
#
# 【問題】
# いま、電光掲示板に `a`, `b`, `c` からなる長さ N の文字列 S が表示されています。
#
# あなたは以下の 2 種類の操作を好きな順番で何回でも行うことができます。ただし 変化させる
# とは、元々 `a` だったものを `b` に、`b` だったものを `c` に、`c` だったものを
# `a` に変えることを指します。
# ・S[i] = `b` である i (1 ≦ i ≦ N) を 1 つ選び、S[i] を `a` に変更した後、S[1], S[2], ..., S[i -
# 1] を変化させる。
# ・S[i] = `c` である i (1 ≦ i ≦ N) を 1 つ選び、S[i] を `b` に変更した後、S[1], S[2], ..., S[i -
# 1] を変化させる。
#
# 最大で何回の操作が行えるか、求めてください。
#
#
# 【制約】
# ・1 ≦ N ≦ 60
# ・S は `a`, `b`, `c` からなる長さ N の文字列である
#
# 【入出力形式】
# 入力形式
# N
# S
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/074
