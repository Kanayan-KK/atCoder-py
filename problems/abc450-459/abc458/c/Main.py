# すべて大文字
s = str(input())
length = len(s)

def find_all_indices(source: str, target: str) -> list[int]:
    if target == "":
        return []

    indices = []
    start = 0

    # 前回の開始位置から1文字進めて、次の一致を検索する
    while True:
        index = source.find(target, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1

    return indices


indexes = find_all_indices(s, "C")
count = 0
for i in indexes:
    min_abs = min(abs(0 - i), abs(length - 1 - i))
    count += 1 + min_abs

print(count)
