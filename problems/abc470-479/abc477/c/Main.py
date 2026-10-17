Q = int(input())
S = str(input())
T = str(input())

# 累積和作成
match = []
for i in range(len(S)):
    if S[i : i + len(T)] == T:
        match.append(1)
    else:
        match.append(0)

prefix = [0]
for i in match:
    prefix.append(prefix[-1] + i)

# print(match)
# print(prefix)

for i in range(Q):
    L, R = map(int, input().split())
    if (R - L + 1) < len(T):
        print("No")
    else:
        print("Yes" if prefix[R - len(T) + 1] - prefix[L - 1] >= 1 else "No")
