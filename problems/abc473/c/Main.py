n, k = map(int, input().split())
nums = list(map(int, input().split()))
dict = {i: 0 for i in range(1, k + 1)}
for num in nums:
    dict[num] += 1

values = dict.values()
max_num = max(values)

ans = 0
for val in values:
    if val >= max_num - 1:
        ans +=1

print(ans)
