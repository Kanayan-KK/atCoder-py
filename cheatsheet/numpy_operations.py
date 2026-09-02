import numpy as np

# NumPyは、大量の数値をまとめて計算するときに使う
# 単純な入出力や要素数の少ない処理では、標準のlistの方が扱いやすい

# ndarrayを作る
numbers = np.array([1, 2, 3, 4])
grid = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((2, 3), dtype=np.int64)
sequence = np.arange(0, 10, 2)
print(numbers)  # [1 2 3 4]
print(zeros)
print(sequence)  # [0 2 4 6 8]

# 形状、次元数、要素の型を確認する
print(grid.shape)  # (2, 3): 2行3列
print(grid.ndim)  # 2
print(grid.dtype)  # int64（環境により表示が異なる場合がある）

# 添字とスライスで要素を取り出す
print(grid[0, 1])  # 2
print(grid[0])  # [1 2 3]
print(grid[:, 1])  # [2 5]: すべての行の1列目

# スライスは元の配列とデータを共有するため、独立させるならcopy()を使う
shared_slice = numbers[1:3]
shared_slice[0] = 20
independent_copy = numbers[1:3].copy()
independent_copy[0] = 99
print(numbers)  # [ 1 20  3  4]
print(independent_copy)  # [99  3]

# 四則演算は要素ごとに行われる
left = np.array([1, 2, 3])
right = np.array([10, 20, 30])
print(left + right)  # [11 22 33]
print(left * right)  # [10 40 90]
print(left**2)  # [1 4 9]

# 大きさ1の次元は自動的に各要素へ広げられる（ブロードキャスト）
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row_offsets = np.array([10, 20, 30])
print(matrix + row_offsets)

# 全体またはaxisごとに集計する
print(matrix.sum())  # 21
print(matrix.sum(axis=0))  # [5 7 9]: 行をまとめ、列ごとに集計
print(matrix.sum(axis=1))  # [ 6 15]: 列をまとめ、行ごとに集計
print(matrix.min(), matrix.max())  # 1 6
print(matrix.mean())  # 3.5

# 条件に合う要素を抽出・置換する
values = np.array([1, 5, 2, 8, 3])
print(values[values >= 3])  # [5 8 3]
print(np.where(values >= 3, values, 0))  # [0 5 0 8 3]

# 形状を変える。reshape()の-1は残りの要素数から自動計算される
flat = np.arange(1, 7)
reshaped = flat.reshape(2, -1)
print(reshaped)
print(reshaped.T)  # 行と列を入れ替える
print(reshaped.ravel())  # 一次元に戻す

# 配列を連結する
first = np.array([[1, 2], [3, 4]])
second = np.array([[5, 6]])
print(np.concatenate([first, second], axis=0))  # 行方向に連結
print(np.concatenate([first, first], axis=1))  # 列方向に連結

# 並べ替えと元の位置を求める
unsorted_values = np.array([30, 10, 20])
print(np.sort(unsorted_values))  # [10 20 30]: 元の配列は変更しない
print(np.argsort(unsorted_values))  # [1 2 0]: 昇順に並ぶ添字

# 行列積には*ではなく@を使う
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print(matrix_a @ matrix_b)

# Pythonのlistへ戻す
print(numbers.tolist())  # [1, 20, 3, 4]
