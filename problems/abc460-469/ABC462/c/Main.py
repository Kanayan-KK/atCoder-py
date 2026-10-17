N = int(input())
Points = list()
Ans = 0
for _i in range(N):
    x, y = map(int, input().split())
    Points.append([x, y])

# x座標でソート
Points.sort()
# print(Points)

minY = N + 1
for _x, y in Points:
    # 最小値更新
    if y < minY:
        minY = y
        Ans += 1
print(Ans)
