from statistics import median

# median(): 値を小さい順に並べたときの中央の値を求める
odd_numbers = [7, 1, 4]
print(median(odd_numbers))  # 4

# 要素数が偶数の場合は、中央にある2つの値の平均になる
even_numbers = [1, 3, 8, 10]
print(median(even_numbers))  # 5.5

# 元のlistは並べ替えられない
numbers = [30, 10, 20]
print(median(numbers))  # 20
print(numbers)  # [30, 10, 20]

# 空のlistでは中央値を求められず、StatisticsErrorになる
# print(median([]))
