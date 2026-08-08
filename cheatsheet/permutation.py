from itertools import permutations
from math import factorial

# permutations(): 要素を並べ替えた全パターンを作る
numbers = [1, 2, 3]
orders = list(permutations(numbers))
print(orders)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3),
#  (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 第2引数で並べる要素数を指定する
pairs = list(permutations(numbers, 2))
print(pairs)
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 文字列の順列はjoin()で文字列に戻す
words = ["".join(order) for order in permutations("ABC")]
print(words)  # ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

# n個すべてを並べるパターン数はn!個
print(factorial(len(numbers)))  # 6

# 元の要素に重複があると同じ順列も生成される
duplicate_orders = list(permutations([1, 1, 2]))
print(len(duplicate_orders))  # 6
print(len(set(duplicate_orders)))  # 重複除去後は3

# パターン数が多い場合はlistにせず、ループで1件ずつ処理する
for order in permutations(numbers):
    print(order)
