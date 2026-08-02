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

# My解答
# N = int(input())
# Takahashis = []
# for _i in range(N):
#     H, L = map(int, input().split())
#     Takahashis.append([H, L])
# Q = int(input())
# TIMES = map(int, input().split())
# for t in TIMES:
#     filtered = [h for h, _l in Takahashis if _l > t + 0.5]
#     print(max(filtered))

# AI解答
from bisect import bisect_right

N = int(input())

heights = []
leave_times = []

for _ in range(N):
    H, L = map(int, input().split())
    heights.append(H)
    leave_times.append(L)

# 答え格納用配列作成
# suffix_max[i]:
# i番目以降の高橋くんの身長の最大値
suffix_max = [0] * N
suffix_max[-1] = heights[-1]

for i in range(N - 2, -1, -1):
    suffix_max[i] = max(heights[i], suffix_max[i + 1])

Q = int(input())
times = map(int, input().split())

for T in times:
    # L > T を満たす最初の位置
    index = bisect_right(leave_times, T)

    print(suffix_max[index])