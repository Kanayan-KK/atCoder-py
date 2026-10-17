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


def check(strings: list[str]) -> bool:
    if all(string == "." for string in strings[0]):
        strings.pop(0)
        return False

    if all(string[0] == "." for string in strings):
        strings[:] = [string[1:] for string in strings]
        return False

    if all(string[-1] == "." for string in strings):
        strings[:] = [string[:-1] for string in strings]
        return False

    if all(string == "." for string in strings[-1]):
        strings.pop()
        return False

    return True


H, W = map(int, input().split())
strings = list()

for _ in range(H):
    strings.append(input())

while not check(strings):
    pass

print("\n".join(strings))
