N = int(input())
ans = N // 2
amari = N % 2
if amari > 0:
    ans += 1
print(ans)
