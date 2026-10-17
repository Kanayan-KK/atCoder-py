from itertools import combinations

N, V = map(int, input().split())
topping_values = list(map(int, input().split()))
happy_by_total: list[tuple[int, int]] = []
for one, two, three in combinations(range(1, N + 1), 3):
    happy = sum([topping_values[one - 1], topping_values[two - 1], topping_values[three - 1]])
    happy_by_total.append((happy, one + two + three))

for happy, total in sorted(happy_by_total, reverse=True):
    if total <= V:
        print(happy)
        break
# sorted_total = sorted(total_by_numbers.items(),reverse=True)
# print(sorted_total_by_nums)
# total_values = [sum(numbers) for numbers in combinations(topping_values, 3)]

# total_values.sort(reverse=True)
# for value in total_values:
#     if value < V:
#         print(value)
#         break
