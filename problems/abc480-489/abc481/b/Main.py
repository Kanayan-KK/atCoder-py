N, K = map(int, input().split())
Ys = list(map(int, input().split()))
ans = sum(Y == K for Y in Ys)
for i in range(N - 1):
    Y = Ys[i]
    nextY = Ys[i + 1]
    if nextY > K > Y or nextY < K < Y:
        ans += 1
    before_y = Y

print(ans)
