# sorted(): 並べ替えた新しいlistを返し、元のデータは変更しない
numbers = [4, 2, 5, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 3, 4, 5]
print(numbers)  # [4, 2, 5, 1, 3]

# list.sort(): 元のlist自体を並べ替え、戻り値はNoneになる
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5]

# reverse=Trueで降順にする
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]

# keyで比較に使う値を指定する
words = ["apple", "fig", "banana"]
print(sorted(words, key=len))  # ['fig', 'apple', 'banana']

# 二次元listは先頭の要素から順に比較される
records = [[2, 80], [1, 90], [2, 70]]
print(sorted(records))  # [[1, 90], [2, 70], [2, 80]]

# 特定の列を基準にする場合はkeyを指定する
print(sorted(records, key=lambda record: record[1]))
# [[2, 70], [2, 80], [1, 90]]

# 複数の条件はtupleで指定する。点数は降順、番号は昇順
scores = [[2, 90], [1, 80], [3, 90]]
print(sorted(scores, key=lambda score: (-score[1], score[0])))
# [[2, 90], [3, 90], [1, 80]]

# 使い分け
# 元のデータを残す、list以外も並べ替える: sorted()
# 元のlistを直接並べ替える: list.sort()
# 降順: reverse=True
# 独自の基準で並べ替える: key=関数
