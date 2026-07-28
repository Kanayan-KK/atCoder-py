# from itertools import combinations

n = int(input())

count = 0
right = 2
range = list(map(int, range(1, n + 1)))

for left in range:
    if left >= right:
        right += 1
    while right <= n:
        print(f"? {left} {right}", flush=True)
        if input() == "Yes":
            right += 1
        else:
            break
    count += right - left + 1

print(f"! {count}", flush=True)
