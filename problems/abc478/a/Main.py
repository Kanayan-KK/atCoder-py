N, M = map(int, input().split())
result = [0 for i in range(N)]
grapes = M
while True:
    if grapes == 0:
        break

    for i in range(N):
        if grapes == 0:
            break
        result[i] += 1
        grapes -= 1

for grape_count in result:
    print(grape_count)
