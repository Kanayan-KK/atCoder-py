# min(): 最小値、max(): 最大値を求める
numbers = [8, 3, 10, 5]
print(min(numbers))  # 3
print(max(numbers))  # 10

# 複数の値を直接渡すこともできる
print(min(8, 3, 10, 5))  # 3
print(max(8, 3, 10, 5))  # 10

# 文字列は辞書順で比較される
words = ["dog", "apple", "cat"]
print(min(words))  # apple
print(max(words))  # dog

# keyで比較に使う値を指定する。返るのは元の要素
temperatures = [-10, 3, 8]
print(min(temperatures, key=abs))  # 3: 絶対値が最小
print(max(temperatures, key=abs))  # -10: 絶対値が最大

# 二次元リストから特定の要素を基準に選ぶ
records = [[1, 80], [2, 95], [3, 70]]
print(min(records, key=lambda record: record[1]))  # [3, 70]
print(max(records, key=lambda record: record[1]))  # [2, 95]

# 最小値や最大値がある位置を求める
min_index = min(range(len(numbers)), key=lambda index: numbers[index])
max_index = max(range(len(numbers)), key=lambda index: numbers[index])
print(min_index)  # 1
print(max_index)  # 2

# 空のデータにはdefaultを指定するとエラーを防げる
empty: list[int] = []
print(min(empty, default=-1))  # -1
print(max(empty, default=-1))  # -1
