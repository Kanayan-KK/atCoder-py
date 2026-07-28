n, m = map(int, input().split())
matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())

    # r行初期化
    matrix[r - 1] = [0] * n

    # c列初期化
    for row in matrix:
        row[c - 1] = 0

    # コマを置く
    matrix[r - 1][c - 1] = 1

count = sum(1 for row in matrix for x in row if x == 1)

# print(matrix)
print(count)
