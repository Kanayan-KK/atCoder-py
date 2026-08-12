# スライス: list[開始位置:終了位置:ステップ]
# 開始位置は含み、終了位置は含まない
values = [0, 1, 2, 3, 4, 5, 6]
print(values[1:4])  # [1, 2, 3]
print(values[:3])  # [0, 1, 2]（先頭から）
print(values[4:])  # [4, 5, 6]（末尾まで）
print(values[1:6:2])  # [1, 3, 5]（2個おき）
print(values[::-1])  # [6, 5, 4, 3, 2, 1, 0]（逆順）
print(values[-3:])  # [4, 5, 6]（末尾から3個）
print(values[4:100])  # [4, 5, 6]（範囲外でもエラーにならない）

# [:]でlistをコピーする
copied_values = values[:]
copied_values[0] = 99
print(values)  # [0, 1, 2, 3, 4, 5, 6]（元のlistは変わらない）
print(copied_values)  # [99, 1, 2, 3, 4, 5, 6]

# スライス代入で指定範囲をまとめて更新する
range_values = [10, 20, 30, 40, 50]
range_values[1:4] = [0] * 3
print(range_values)  # [10, 0, 0, 0, 50]

# スライス代入では要素数を変えられる
range_values[1:4] = [99]
print(range_values)  # [10, 99, 50]

# 使い分け
# 一部分を取得: values[start:stop]
# 一定間隔で取得: values[start:stop:step]
# 逆順の新しいlistを作る: values[::-1]
# 指定範囲をまとめて更新: values[start:stop] = new_values
