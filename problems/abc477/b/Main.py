N, D = map(int, input().split())
x_nums = list(map(int, input().split()))
result: list[int] = []
for i, num in enumerate(x_nums):
    if all(abs(v - num) >= D for index, v in enumerate(x_nums) if index != i):
        result.append(i + 1)

sorted(result)
print(len(result))
print(*result)
