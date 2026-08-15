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

# 重複除去や高速な存在確認に使う
