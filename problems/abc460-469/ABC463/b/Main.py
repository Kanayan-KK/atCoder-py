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
n,X = map(str,input().split())
N = int(n)
x = 0
if X == "A":
    x = 0
if X == "B":
    x = 1
if X == "C":
    x = 2
if X == "D":
    x = 3
if X == "E":
    x = 4
canReserve = False
for _i in range(N):
    S = str(input())
    if S[x] == "o":
        canReserve = True

print("Yes" if canReserve else "No")