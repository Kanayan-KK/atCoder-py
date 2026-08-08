from collections import Counter

numbers = [1, 2, 3, 4, 5, 6]

# 条件が True になる要素の数を数える
even_count = sum(number % 2 == 0 for number in numbers)
print(even_count)  # 3

greater_than_three_count = sum(number > 3 for number in numbers)
print(greater_than_three_count)  # 3

fruits = ["apple", "orange", "apple", "banana"]

# list.count(): 指定した値と完全に一致する要素を数える
apple_count = fruits.count("apple")
print(apple_count)  # 2

# Counter(): すべての値を種類別にまとめて数える
fruit_counts = Counter(fruits)
print(fruit_counts)  # Counter({'apple': 2, 'orange': 1, 'banana': 1})
print(fruit_counts["orange"])  # 1
print(fruit_counts["grape"])  # 0

# 使い分け
# 条件に合う要素を数える: sum()
# 1つの値を数える: list.count()
# 複数の値を種類別に数える: Counter()
