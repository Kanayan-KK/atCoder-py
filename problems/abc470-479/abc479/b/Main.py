N = int(input())
S = str(input())
ans = 0
for i in range(len(S),0,-1):
    if "R" * i in S:
        ans = i
        break
print(ans)