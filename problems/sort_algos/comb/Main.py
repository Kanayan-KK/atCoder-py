# コムソート(https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%A0%E3%82%BD%E3%83%BC%E3%83%88)
# 1. 総数 n を 1.3 で割り、小数点以下を切り捨てた数を間隔 h とする。
# 2. i=0 とする。
# 3. i 番目と i+h 番目を比べ、i+h 番目が小さい場合入れ替える。
# 4. i=i+1 とし、i+h>n となるまで3を繰り返す。
# 5. hがすでに1になっている場合は入れ替えが発生しなくなるまで上の操作を繰り返す。
# 6. h を 1.3 で割り、小数点以下を切り捨てた数を新たに間隔 h とし、操作を繰り返す。

# 数列
numbers = list(map(int, input().split()))

# 総数
n = len(numbers)

# 間隔
# float > int 型変換で小数点以下を切り捨て
h = max(1, int(n / 1.3))

# 入れ替え発生フラグ
changed = True


# 手順 1 - 4
def comb() -> bool:
    result = False
    # i + h > n
    for i in range(n - h):
        # i 番目と i+h 番目を比べ、i+h 番目が小さい場合入れ替える
        if numbers[i] > numbers[i + h]:
            numbers[i], numbers[i + h] = numbers[i + h], numbers[i]
            result = True
    return result


# h > 1 の間は繰り返す
# h == 1 になっても入れ替えが発生しなくなるまでは繰り返す
while True:
    changed = comb()
    if h > 1:
        h = int(h / 1.3)
        continue
    if h == 1:
        if not changed:
            break


print(" ".join(map(str, numbers)))

# 出力：
# 1 2 4 5 8
# 実行時間：61.923 ms
# 使用メモリ：27312 KiB
# 判定：OK

# 出力：
# -1 -1 0 2 2 3 3
# 実行時間：60.045 ms
# 使用メモリ：27320 KiB
# 判定：OK

# 出力：
# 1 2 3 4 5 6
# 実行時間：59.088 ms
# 使用メモリ：27292 KiB
# 判定：OK

# 出力：
# -1000000000 -999999999 -42 7 10 42 1000 123456789 999999999 1000000000
# 実行時間：60.322 ms
# 使用メモリ：27264 KiB
# 判定：OK

# 出力：
# 実行時間：66.997 ms
# 使用メモリ：29328 KiB
# 判定：OK

# 良い点：遠く離れた位置の数値を移動させる必要がある時
# 少ない手順で移動させられるので実行速度が速い
