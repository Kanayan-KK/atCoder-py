n = int(input())
ans = 0
strings = []
for i in range(n):
    strings.append(input().lower())

for string in strings:
    ans = max(ans, strings.count(string))

print(ans)