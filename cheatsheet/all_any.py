values = [True, True, False]

# all(): すべての要素が True なら True
print(all(values))  # False

# any(): 1つでも True の要素があれば True
print(any(values))  # True

numbers = [2, 4, 6]

# 各要素を条件式で判定する使い方
print(all(number % 2 == 0 for number in numbers))  # True
print(any(number > 5 for number in numbers))  # True
