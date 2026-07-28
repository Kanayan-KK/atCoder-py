N = int(input())
X = list(map(int, input().split()))
print("Yes" if all(X[i] < 0 for i in range(N - 1)) else "No")
