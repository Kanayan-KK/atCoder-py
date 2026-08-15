# 複数のlistを順番どおりにマージする
left_values = [1, 2]
right_values = [2, 3]
merged_values = left_values + right_values
print(merged_values)  # [1, 2, 2, 3]（重複も残る）
print(left_values)  # [1, 2]（元のlistは変わらない）

# extend()は呼び出したlist自体を変更する
left_values.extend(right_values)
print(left_values)  # [1, 2, 2, 3]

# 入れ子のlistを1段だけ平らにしてマージする
groups = [[1, 2], [3], [4, 5]]
flattened_values = [value for group in groups for value in group]
print(flattened_values)  # [1, 2, 3, 4, 5]

# マージ方法の使い分け
# 元のlistを残して新しく作る: left + right
# 元のlistへ追加する: left.extend(right)
# 入れ子を1段平らにする: [value for group in groups for value in group]
