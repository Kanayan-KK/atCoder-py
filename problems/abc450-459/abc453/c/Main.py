# n = int(input())
# l_list = list(map(float, input().split()))
# current = 0.5
# ans = 0
# for l_num in l_list:
#     b_sign = 1 if current > 0 else -1
#     current = current + (b_sign * -1) * l_num
#     a_sign = 1 if current > 0 else -1
#     if b_sign != a_sign:
#         ans += 1

# print(ans)

n = int(input())
l_list = list(map(int, input().split()))

ans = 0


def dfs(i, current, count):
    global ans

    if i == n:
        ans = max(ans, count)
        return

    l = l_list[i] * 2

    # 正の方向
    next_pos = current + l
    dfs(i + 1, next_pos, count + (current < 0 < next_pos))

    # 負の方向
    next_pos = current - l
    dfs(i + 1, next_pos, count + (current > 0 > next_pos))


dfs(0, 1, 0)

print(ans)