# N:宝石の個数
# K:N個の宝石から取る数
# M:N個の宝石から取る宝石の色の種類
N, K, M = map(int, input().split())

# 宝石価値総和の取りうる最大値
# ans = 0

# 入力値取得
values = list()
for _i in range(N):
    c, v = map(int, input().split())
    values.append([c, v])

# 価値で降順ソート
values.sort(key=lambda x: x[1], reverse=True)

unique_nums = list()
duplicate_nums = list()
used_colors = set()

for c, v in values:

    # 価値が高い順に上位Kを追加する
    if len(unique_nums) + len(duplicate_nums) < K:
        if c in used_colors:
            duplicate_nums.append(v)
        else:
            used_colors.add(c)
            unique_nums.append(v)
    else:
        # ループ終了条件
        if len(used_colors) >= M:
            break

        # 重複している色は無視
        if c in used_colors:
            continue

        # 重複している最低値のものを削除
        duplicate_nums.pop()

        used_colors.add(c)
        unique_nums.append(v)

print(sum(unique_nums) + sum(duplicate_nums))
