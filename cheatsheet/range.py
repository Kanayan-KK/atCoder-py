# range(): 一定間隔の整数列を表す。stopは含まない
# range(stop): 0からstop未満まで。開始値は0、増減量は1
print(list(range(5)))  # [0, 1, 2, 3, 4]

# range(start, stop): startからstop未満まで
print(list(range(2, 6)))  # [2, 3, 4, 5]

# range(start, stop, step): stepずつ増減する
print(list(range(1, 8, 2)))  # [1, 3, 5, 7]
print(list(range(0, 10, 3)))  # [0, 3, 6, 9]

# 降順は負のstepを指定する。stopより大きい間だけ続く
print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]
print(list(range(6, -1, -2)))  # [6, 4, 2, 0]

# AtCoderでよく使う範囲: 0〜n-1、1〜n、n-1〜0
n = 4
print(list(range(n)))  # [0, 1, 2, 3]
print(list(range(1, n + 1)))  # [1, 2, 3, 4]
print(list(range(n - 1, -1, -1)))  # [3, 2, 1, 0]

# 回数だけ必要な場合は、使わない変数を_にする
for _ in range(3):
    print("Hello")  # Helloを3回出力

# 添字を使ってリストの要素を更新する
values = [10, 20, 30]
for index in range(len(values)):
    values[index] += index
print(values)  # [10, 21, 32]

# rangeはリストではなく、全要素を保持しない省メモリな整数列
# 内容の表示やリストとしての編集が必要なときだけlist()に変換する
numbers = range(2, 10, 2)
print(numbers)  # range(2, 10, 2)
print(list(numbers))  # [2, 4, 6, 8]
print(list(numbers))  # [2, 4, 6, 8]（繰り返し利用できる）

# 長さ・添字・スライス・整数の所属判定が使える
print(len(numbers))  # 4
print(numbers[0], numbers[-1])  # 2 8
print(list(numbers[1:3]))  # [4, 6]
print(6 in numbers, 7 in numbers)  # True False
print(sum(numbers))  # 20

# 開始時点で範囲外なら空になる。降順はstepを省略できない
print(list(range(0)))  # []
print(list(range(3, 3)))  # []
print(list(range(5, 2)))  # []
print(list(range(2, 5, -1)))  # []

# step=0はValueError。引数に小数を渡すとTypeError
# range(0, 5, 0)
# range(0, 2.5)

# 使い分け
# 決まった回数や一定間隔の整数: range()
# 要素だけ必要: for value in values
# 添字と要素が必要: enumerate(values)
# 既存の列を逆順に読む: reversed(values)
# 終了回数が未定: while（ループ全般はloop.pyを参照）
