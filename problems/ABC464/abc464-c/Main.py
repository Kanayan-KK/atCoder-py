# from collections import deque
# from collections import Counter
# from itertools import combinations
# from itertools import permutations
# from itertools import accumulate
# from math import gcd, lcm
# from math import sqrt
# from math import factorial
# from math import comb
# from math import perm

N, M = map(int, input().split())
nums = list()
for i in range(1, N + 1):
    # temp = list()
    a, d, b = map(int, input().split())
    if d == i:
        a = b
    nums.append(a)
print(nums)
