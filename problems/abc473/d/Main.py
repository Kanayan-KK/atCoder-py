# from itertools import permutations

# n, k = map(int, input().split())
# stack = [0 for i in range(n)]

# def dfs (stack:list[int]):
#     result = 0
#     for i,num in enumerate(stack):
#         result += (i+1) * num
#     if result == n:
#         print(" ".join(map(str,stack)))

#     for x in range(k):
#         stack.app

# dfs(stack)
# coms = list(permutations(range(k + 1), n))

# for com in coms:
#     sum = 0
#     for i, num in enumerate(com):
#         sum += (i + 1) * num
#     if sum == k:
#         print(com)
