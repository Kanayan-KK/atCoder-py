# from collections import deque

n, q = map(int, input().split())

# TLE
# nums = deque(map(int, input().split()))
# for _i in range(q):
#     a = int(input())
#     nums.remove(a)
#     nums.append(a)
# print(" ".join(map(str, nums)))

nums = list(map(int, input().split()))
nums_dict = {num: None for num in nums}
# print(nums_dict)
for _i in range(q):
    a = int(input())
    del nums_dict[a]
    nums_dict[a] = None
    # print(nums_dict)

print(*nums_dict)