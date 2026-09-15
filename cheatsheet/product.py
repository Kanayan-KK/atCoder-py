from itertools import product

# product(): 各候補から1個ずつ選ぶ直積を作る（多重for文と同じ）
# 結果はタプルで、右側の候補から順に切り替わる
pairs = list(product([1, 2], "AB"))
print(pairs)  # [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

# repeat=長さ: 同じ候補を繰り返し使う。位置ごとに同じ値を選んでもよい
# product([0, 1], repeat=2)はproduct([0, 1], [0, 1])と同じ
patterns = list(product([0, 1], repeat=2))
print(patterns)  # [(0, 0), (0, 1), (1, 0), (1, 1)]

# 文字列の全パターンはjoin()で文字列に戻す
words = ["".join(chars) for chars in product("AB", repeat=2)]
print(words)  # ['AA', 'AB', 'BA', 'BB']

# 各桁で候補が異なる場合は、*で候補リストを引数に展開する
choices = [[1, 2], [10], [100, 200]]
print(list(product(*choices)))
# [(1, 10, 100), (1, 10, 200), (2, 10, 100), (2, 10, 200)]

# AtCoderでの全探索: 各要素を選ぶ・選ばないの全パターンを試す
numbers = [2, 3, 5]
target = 5
for flags in product([0, 1], repeat=len(numbers)):
    total = sum(value for value, flag in zip(numbers, flags, strict=True) if flag)
    if total == target:
        print(flags)  # (0, 0, 1)、(1, 1, 0)

# 件数は候補数の積。同じ候補m個をn回使う場合はm**n個になる
# 大量の結果はlistにせず1件ずつ処理する（全探索の時間は減らない）
# 入力の候補は内部で保持するため、無限イテレータは渡さない
for row, col in product(range(2), range(2)):
    print(row, col)  # 0 0 → 0 1 → 1 0 → 1 1

# 戻り値はイテレータなので、一度取り出した結果は再利用できない
iterator = product([1, 2], repeat=1)
print(list(iterator))  # [(1,), (2,)]
print(list(iterator))  # []

# 入力の重複はそのまま残る
print(list(product([1, 1], [2])))  # [(1, 2), (1, 2)]

# 候補に空の入力があれば0件。repeat=0は空タプル1件
print(list(product([], [1, 2])))  # []
print(list(product([1, 2], repeat=0)))  # [()]

# 使い分け（候補の値が重複していない場合）
# product: 同じ値を何度でも選べる。順序を区別する
# permutations: 同じ要素を再利用せず並べる。順序を区別する
# combinations: 同じ要素を再利用せず選ぶ。順序を区別しない
