# for: リストなどの要素を順番に取り出す
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# range(stop): 0以上stop未満の整数を繰り返す
for number in range(3):
    print(number)  # 0, 1, 2

# range(start, stop, step): 開始値、終了値、増減量を指定する
for number in range(2, 7, 2):
    print(number)  # 2, 4, 6

for number in range(3, 0, -1):
    print(number)  # 3, 2, 1

# enumerate(): 要素とインデックスを同時に取り出す
for index, fruit in enumerate(fruits):
    print(index, fruit)  # 0 apple, 1 banana, 2 orange

# zip(): 複数のリストから同じ位置の要素を取り出す
scores = [80, 90, 75]
for fruit, score in zip(fruits, scores, strict=True):
    print(fruit, score)

# while: 条件がTrueの間だけ繰り返す
count = 3
while count > 0:
    print(count)  # 3, 2, 1
    count -= 1  # 更新を忘れると無限ループになる

# continue: 条件に合う回だけ残りの処理を飛ばす
for number in range(5):
    if number % 2 == 0:
        continue
    print(number)  # 1, 3

# break: 条件に合った時点でループを終了する
numbers = [4, 7, 10, 13]
for number in numbers:
    if number % 5 == 0:
        print(number)  # 10
        break

# 二重ループ: 行と列の組み合わせを順番に処理する
for row in range(2):
    for column in range(3):
        print(row, column)

# 使い分け
# 要素や決まった回数を順番に処理する: for
# 条件を満たす間だけ繰り返す: while
# インデックスも必要: enumerate()
# 複数の列を同時に処理する: zip()
