N = int(input())
S = input()
T = input()

result = True
for i in range(N):
    if S[i] != T[i] and T[i] != "*":
        result = False
        break

print("Yes" if result else "No")