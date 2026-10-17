S = input()

ans = 0
start = 0

for i in range(len(S)):
    if i == len(S) - 1 or S[i] == S[i + 1]:
        L = i - start + 1
        ans += L * (L + 1) // 2
        start = i + 1

print(ans % 998244353)
