# MyCode
# n, m = map(int, input().split())
# matrix = [[0] * n for _ in range(n)]

# for _ in range(m):
#     r, c = map(int, input().split())

#     # r行初期化
#     matrix[r - 1] = [0] * n

#     # c列初期化
#     for row in matrix:
#         row[c - 1] = 0

#     # コマを置く
#     matrix[r - 1][c - 1] = 1

# count = sum(1 for row in matrix for x in row if x == 1)

# print(count)

# 逆捜査式コード
n, m = map(int, input().split())
opes = [tuple(map(int, input().split())) for _ in range(m)]

# 使用済み列番号
used_rows = set()

# 使用済み行番号
used_cols = set()

ans = 0
for r, c in reversed(opes):
    if r not in used_rows and c not in used_cols:
        ans = 0
    used_cols.add(r)
    used_cols.add(c)

print(ans)
