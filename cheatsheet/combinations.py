from itertools import combinations
from math import comb

# combinations(): 順序を区別せず、指定した個数を選ぶ
numbers = [1, 2, 3, 4]
pairs = list(combinations(numbers, 2))
print(pairs)
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# (1, 2)と(2, 1)は同じ組み合わせなので、片方だけ生成される
triples = list(combinations(numbers, 3))
print(triples)
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

# 文字列の組み合わせはjoin()で文字列に戻す
words = ["".join(group) for group in combinations("ABC", 2)]
print(words)  # ['AB', 'AC', 'BC']

# n個からr個を選ぶ組み合わせ数はmath.comb(n, r)で求める
print(comb(len(numbers), 2))  # 6

# 元の要素に重複があると同じ値の組み合わせも生成される
duplicate_pairs = list(combinations([1, 1, 2], 2))
print(duplicate_pairs)  # [(1, 1), (1, 2), (1, 2)]
print(set(duplicate_pairs))  # {(1, 1), (1, 2)}

# 件数が多い場合はlistにせず、ループで1件ずつ処理する
for pair in combinations(numbers, 2):
    print(pair)
