# マージソート(分割統治法)(https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%BC%E3%82%B8%E3%82%BD%E3%83%BC%E3%83%88)
# 1. データ列を分割する（通常、二等分する）
# 2. 分割された各データ列で、含まれるデータが1個ならそれを返し、2個以上ならステップ1から3を再帰的に適用してマージソートする
# 3. 二つのソートされたデータ列（1個であればそれ自身）をマージする

numbers = list(map(int, input().split()))


def merge_sort(array: list[int]):
    n = len(array)
    if n <= 1:
        return array

    # 中央のインデックスを求める
    mid = len(array) // 2

    # 左右に分割
    left = array[:mid]
    right = array[mid:]

    # 左に再帰処理
    left = merge_sort(left)

    # 右に再帰処理
    right = merge_sort(right)

    # 左右をマージ
    return merge(left, right)


def merge(left: list[int], right: list[int]):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        # 左右の先頭を比較
        l_first = left[i]
        r_first = right[j]
        if l_first <= r_first:
            result.append(l_first)
            i += 1
        else:
            result.append(r_first)
            j += 1
    result += left[i:] + right[j:]
    return result


result = merge_sort(numbers)
print(" ".join(map(str, result)))
