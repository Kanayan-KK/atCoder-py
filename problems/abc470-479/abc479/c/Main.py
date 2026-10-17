N, W = map(int, input().split())
delicious = []
volume = []
for _i in range(N):
    deli, vol = map(int, input().split())
    delicious.append(deli)
    volume.append(vol)

# DPはW = 10^9 なので使えない
# # dp = [[0] * (W + 1) for _i in range(N + 1)]
# dp = [0] * (W + 1)

# for i in range(N):
#     for j in range(W, volume[i] - 1, -1):
#         # i番目のおかずを選ばない
#         dp[j] = max(dp[j], dp[j - volume[i] + delicious[i]])

#         # # i番目のおかずを選ぶ
#         # if j + volume[i] <= W:
#         #     dp[i + 1][j + volume[i]] = max(dp[i + 1][j + volume[i]], dp[i][j] + delicious[i])

#         # print(dp[i])

# print(max(dp))

# N <= 20 なのでbit全探索
ans = 0
for bit in range(1 << N):
    total_deli = 0
    total_vol = 0
    for i in range(N):
        if bit & (1 << i):
            total_deli += delicious[i]
            total_vol += volume[i]
    if total_vol <= W:
        ans = max(ans, total_deli)

print(ans)