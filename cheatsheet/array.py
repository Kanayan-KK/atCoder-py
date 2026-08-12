from collections import deque

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

# list.pop(): 位置を省略すると末尾から取り出す
list_items = ["A", "B", "C"]
print(list_items.pop())  # C
print(list_items.pop(0))  # A（先頭から取り出せるが、大きなlistでは遅い）

# tuple: 順序あり、変更不可、重複可能
point = (3, 5)
x, y = point
print(x, y)  # 3 5
# tupleには要素を追加できない
# point[0] = 10  # 変更できないためエラー

# queue: 先に追加した要素から取り出す（FIFO）
queue = deque(["A", "B"])
queue.append("C")  # 右端（末尾）に追加
print(queue.popleft())  # A（左端の最初に入れた要素）
print(queue)  # deque(['B', 'C'])

# deque.pop(): 右端から取り出すためFIFOにはならない
print(queue.pop())  # C
print(queue)  # deque(['B'])

# set: 順序なし、重複不可、変更可能
unique_numbers = set([1, 2, 2, 3])
unique_numbers.add(4)  # 順序がないため追加位置は決まらない
unique_numbers.discard(1)
print(2 in unique_numbers)  # True
print(len(unique_numbers))  # 3

# set同士の集合演算
left = {1, 2, 3}
right = {3, 4, 5}
print(left | right)  # 和集合: {1, 2, 3, 4, 5}
print(left & right)  # 共通部分: {3}

# 使い分け
# 一般的な配列: list
# 変更しない組: tuple
# 追加順に処理: deque
# 重複除去や高速な存在確認: set
