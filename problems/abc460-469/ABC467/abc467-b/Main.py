n = int(input())
count = 0
for _ in range(n):
    a, b, s = input().split()
    a, b = map(int, [a, b])
    if s == "keep":
        count += b - a
print(count)
