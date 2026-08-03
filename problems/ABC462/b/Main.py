N = int(input())
result = [set() for i in range(N)]
for i in range(N):
    for index, value in enumerate(map(int, input().split())):
        if index != 0:
            result[value - 1].add(i + 1)

for values in result:
    print(len(values), " ".join(map(str, values)))
