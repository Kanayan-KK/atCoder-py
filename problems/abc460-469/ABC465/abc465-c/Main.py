# 解答1:実行時間超過する
# N = int(input())
# S = str(input())

# ans = list(map(int, range(1, N + 1)))

# for k in range(1, len(S) + 1):
#     s = S[k - 1]
#     if s == "o":
#         ans[0:k] = reversed(ans[0:k])
# print(" ".join(map(str, ans)))

# 解答2:毎回のreverseで時間がかかっているのでを毎回やらない
from collections import deque

N = int(input())
S = str(input())

ans = deque()
isReverse = False
for k, s in enumerate(S, start=1):
    if isReverse:
        ans.appendleft(k)
    else:
        ans.append(k)

    if s == "o":
        isReverse = not isReverse

if isReverse:
    ans.reverse()

print(*ans)
