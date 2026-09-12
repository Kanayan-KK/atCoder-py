# 027 - Sign Up Requests （★2）
# 問題画像: 027.jpg
# 問題・提出: https://atcoder.jp/contests/typical90/tasks/typical90_aa
# 出典: https://github.com/E869120/kyopro_educational_90
# サンプル出典: https://github.com/E869120/kyopro_educational_90/blob/main/sample/027.txt
#
# 【問題】
# 低橋君は、競技プログラミングのサイト「LowCoder」を作り、サービスを開始しました。
# 今日の時点では、「LowCoder」にユーザーはいません。
#
# 今日から数えて i (1≦i≦N) 日後には、ユーザー名 S[i]
# を希望するユーザーが登録申請を行い、次のことが起こります。
# ・その時点でユーザー名が S[i] であるユーザーが存在する場合、その登録申請は無視されます。
# ・一方、存在しない場合は登録申請が受理され、LowCoder にそのユーザーが登録されます。
#
# 登録申請が受理されたのが、何日目に登録申請を行ったユーザーなのか、小さい順に出力せよ。
#
# 【制約】
# ・1 ≦ N ≦ 10^5
# ・1 ≦ |S[i]| ≦ 15
# S[i] は英小文字または数字から成る
# ・N は整数
#
# 【入出力形式】
# 入力形式
# N
# S[1]
# S[2]
#  :
# S[N]
#
# 【サンプルテスト】解答を書いた後、リポジトリのルートで実行する。
# .\scripts\test-samples.ps1 problems/educational_90/027
