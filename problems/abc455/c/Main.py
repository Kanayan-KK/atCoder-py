from collections import Counter

n, k = map(int, input().split())
nums = list(map(int, input().split()))
counts = Counter(nums)
num_sum = sorted(
    [[num, num * counts[num]] for num in sorted(counts, reverse=True)],
    key=lambda num_sum: num_sum[1],
    reverse=True,
)
print(sum(sum for num, sum in num_sum[k:]))
