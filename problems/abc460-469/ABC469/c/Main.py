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
for k in range(1, N + 1):
    s = S
    # 食べたお菓子の数
    ans = 0
    # 現在持っているxの数
    xCount = 1
    for i in range(N):
        # 列にまだk個袋が残っていて、かつ「当たり」と書かれた袋を持っている場合にしか行動はできない
        if "o" in s and xCount >= 1 and len(s) >= 1:
            ans += min(len(s), k)

            # x を一個捨てる
            xCount -= 1

            # 先頭から k 個まで取得
            target = s[:k]

            xCount += target.count("o")
            s = s[k:]
        else:
            break

    print(ans)
