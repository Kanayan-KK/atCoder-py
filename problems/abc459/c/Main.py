n, q = map(int, input().split())

block = [0] * n
count = [0] * (q + 1)
offset = 0

for _ in range(q):
    id, num = input().split()
    number = int(num)

    if id == "1":
        x = number - 1

        block[x] += 1
        count[block[x]] += 1

        if count[block[x]] == n:
            offset = block[x]

    else:
        if offset + number > q:
            print(0)
        else:
            print(count[offset + number])
