x, y, l, r, a, b = map(int, input().split())
ans = 0
for h in range(a, b):
    if l <= h < r:
        ans += x
    else:
        ans += y
print(ans)
