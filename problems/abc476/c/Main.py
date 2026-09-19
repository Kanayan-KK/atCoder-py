from collections import deque
import heapq

N = int(input())
# numbers = deque(map(int, input().split()))
# max_heap = []

# numbers = list(map(int, input().split()))
# sorted_numbers = sorted(numbers, reverse=True)
# last_i = len(sorted_numbers) - 1
# print_count = 0
# for i in range(N):
#     heapq.heappush(max_heap, -numbers.popleft())
#     if i > 1:
#         print(-max_heap[len(max_heap) - 1])

n = int(input())
a = list(map(int, input().split()))
s = a[:3]
s.sort(reverse=True)
print(s[2])
for k in range(3, n):
    s.append(a[k])
    s.sort(reverse=True)
    s.pop()
    print(s[2])