n, m = map(int, input().split())
result = [-1] * m
for i in range(n):
    c, s = map(int, input().split())
    if result[c - 1] < s:
        result[c - 1] = s
result = map(str, result)
print(" ".join(result))
