N, Q = map(int, input().split())
list_k = list(map(int, input().split()))
nums = list(i for i in range(1, N + 1))

# print(nums)
for k in list_k:
    nums = [-x for x in nums[:k][::-1]] + nums[k:]
    # print(nums)

for num in nums:
    print(num)