# list: 順序あり、変更可能、重複可能
numbers = [10, 20, 20]
numbers.append(30)  # 末尾に追加
numbers[0] = 5
print(numbers)  # [5, 20, 20, 30]
print(numbers[1])  # 20

# 一次元配列を初期化する
empty_values = []
zero_values = [0] * 5
index_values = list(range(5))
square_values = [index**2 for index in range(5)]
print(empty_values)  # []
print(zero_values)  # [0, 0, 0, 0, 0]
print(index_values)  # [0, 1, 2, 3, 4]
print(square_values)  # [0, 1, 4, 9, 16]

# 二次元配列は行ごとに別のlistを作る
rows = 3
columns = 4
grid = [[0] * columns for _ in range(rows)]
grid[0][1] = 9
print(grid)  # [[0, 9, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# [[0] * columns] * rowsでは同じ行が共有されるため使わない
shared_grid = [[0] * columns] * rows
shared_grid[0][1] = 9
print(shared_grid)  # [[0, 9, 0, 0], [0, 9, 0, 0], [0, 9, 0, 0]]

# 初期化の使い分け
# 空のlist: []
# 同じ値を並べる: [value] * length
# 連番を作る: list(range(length))
# 値を計算して作る: [expression for ...]
# 二次元配列: [[value] * columns for _ in range(rows)]

# 要素を追加する
list_items = ["A", "B"]
list_items.append("C")  # 末尾に1要素を追加
list_items.extend(["D", "E"])  # 末尾に複数要素を追加
list_items.insert(1, "X")  # 指定位置に追加
print(list_items)  # ['A', 'X', 'B', 'C', 'D', 'E']

# pop(): 指定位置から削除し、削除した値を返す
print(list_items.pop())  # E（位置を省略すると末尾）
print(list_items.pop(1))  # X
print(list_items.pop(0))  # A（先頭の操作は、大きなlistでは遅い）
print(list_items)  # ['B', 'C', 'D']

# remove(): 最初に一致した値を削除する
duplicate_items = [10, 20, 10, 30]
duplicate_items.remove(10)
print(duplicate_items)  # [20, 10, 30]

# del: 値を返さず、位置や範囲を指定して削除する
del_items = [10, 20, 30, 40, 50]
del del_items[1]
del del_items[1:3]
print(del_items)  # [10, 50]

# clear(): すべての要素を削除する
del_items.clear()
print(del_items)  # []

# 操作の使い分け
# 末尾に1要素を追加: append(value)
# 末尾に複数要素を追加: extend(values)
# 指定位置に追加: insert(index, value)
# 削除した値も使う: pop(index)
# 最初に一致した値を削除: remove(value)
# 位置や範囲を削除: del values[index_or_slice]
# すべて削除: clear()
# 空のlistでpop()するとIndexError、存在しない値をremove()するとValueErrorになる
