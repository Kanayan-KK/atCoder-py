N = int(input())
numbers = map(int, input().split())
result = 0
for i,num in enumerate(numbers):
    i += 1
    if i % 2 != 0:
        result += num
print(result)