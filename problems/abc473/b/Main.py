n = int(input())
nums = list(map(int, input().split()))
unique_nums = set(nums)
ans = 0

for num in unique_nums:
    c = nums.count(num) % 2
    ans += num * c

print(ans)
