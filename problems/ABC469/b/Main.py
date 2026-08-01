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
N = int(input())
S = str(input())
ans = 0
for i in range(N):
    if S[i] == "x":
        if S[max(0, i - 1)] == "x" and S[min(N - 1, i + 1)] == "x":
            ans += 1
print(ans)
