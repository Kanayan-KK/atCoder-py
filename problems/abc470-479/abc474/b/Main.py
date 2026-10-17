n = int(input())
p_nums = list(map(int, input().split()))
is_ruled = True
for i, num in enumerate(p_nums):
    group = i // 10 + 1
    if num > group * 10:
        is_ruled = False

print("Yes" if is_ruled else "No")
    
