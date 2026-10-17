# from statistics import median

# x = int(input())
# q = int(input())

# nums = [x]

# for _i in range(q):
#     a, b = map(int, input().split())
#     nums += [a, b]
#     print(median(nums))

import heapq

x = int(input())
q = int(input())

# low: 小さい側（max heapとして使いたいので負数）
# high: 大きい側（min heap）
low = [-x]
high = []


def add(x):
    if x <= -low[0]:
        heapq.heappush(low, -x)
    else:
        heapq.heappush(high, x)

    # サイズ調整
    if len(low) > len(high) + 1:
        heapq.heappush(high, -heapq.heappop(low))

    if len(low) < len(high):
        heapq.heappush(low, -heapq.heappop(high))


for _ in range(q):
    a, b = map(int, input().split())

    add(a)
    add(b)

    print(-low[0])
