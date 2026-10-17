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

N, K = map(int, input().split())
trains = list(map(int,range(1, N + 1)))
trains.reverse()

for num,i in enumerate(trains,1):
    if num == K:
        print(i)
