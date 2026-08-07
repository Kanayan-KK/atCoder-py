N, M = map(int, input().split())
listA = list(map(int, input().split()))
N = len(listA)
listB = list(map(int, input().split()))
M = len(listB)

listA.sort()
listB.sort()

sushi_count = 0
j = 0
for a in listA:
    if j >= M:
        break
    if 2 * a >= listB[j]:
        j += 1
        sushi_count += 1

print(sushi_count)
