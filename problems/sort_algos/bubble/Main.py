# バブルソート(https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%96%E3%83%AB%E3%82%BD%E3%83%BC%E3%83%88)
# 全ての要素に関して、隣接する要素と比較し順序が逆であれば入れ替える。
# これを要素数-1回繰り返すことでソートを行う。
# なおこの繰り返しは、入れ替えが起こらなくなった時点で中断することができる。

# 数列
numbers = list(map(int, input().split()))

# 要素数
n = len(numbers)

# 入れ替え処理(昇順)
def bubble():
    changed = False
    for i in range(n - 1):
        if numbers[i + 1] < numbers[i]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            if not changed:
                changed = True
    return changed


# n - 1 回処理を呼ぶ
for _i in range(n - 1):
    if not bubble():
        # 入れ替えが起こらなくなったら中断
        break

print(" ".join(map(str, numbers)))

# 出力：
# 1 2 4 5 8
# 実行時間：75.479 ms
# 使用メモリ：28136 KiB
# 判定：OK

# 出力：
# -1 -1 0 2 2 3 3
# 実行時間：78.313 ms
# 使用メモリ：28196 KiB
# 判定：OK

# 出力：
# 1 2 3 4 5 6
# 実行時間：77.170 ms
# 使用メモリ：28296 KiB
# 判定：OK

# 出力：
# -1000000000 -999999999 -42 7 10 42 1000 123456789 999999999 1000000000
# 実行時間：77.233 ms
# 使用メモリ：28216 KiB
# 判定：OK

# 計算量 : O(N^2-1)