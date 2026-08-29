n = int(input())
nums = list(map(int, input().split()))

start = n // 2
ans = 0

for i in range(start, n):
    ans += nums[i]

print(ans)