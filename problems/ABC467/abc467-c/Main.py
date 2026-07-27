# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = 0

# for x in range(n):
#     for i in range(1, n - 1):
#         if (a[i - 1] + a[i]) / m != b[i - 1]:
#             a[x - 1] += 1
#         else:
#             print(c)


# TYPE1
# N, _M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# # 先頭を 0 とした場合に必要な最終状態
# current = 0
# changes = int(A[0] != current)

# for i in range(N - 1):
#     current = B[i] ^ current
#     changes += int(A[i + 1] != current)

# # もう一方の候補は全要素が反転する
# print(min(changes, N - changes))

# TYPE2
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 先頭が 0 と 1 の場合を両方調べる
answer = N

for first_value in [0, 1]:
    target = [first_value]

    # 問題文の条件を満たす次の値を探す
    for i in range(N - 1):
        for next_value in [0, 1]:
            total = target[i] + next_value
            remainder = total % M

            if remainder == B[i]:
                target.append(next_value)
                break

    # 元の A と異なる場所を数える
    operations = 0

    for i in range(N):
        if A[i] != target[i]:
            operations += 1

    # 最小回数を更新する
    if operations < answer:
        answer = operations

print(answer)