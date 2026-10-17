n = int(input())
values = map(int, input().split())
minus = []
plus = []
for value in values:
    if value < 0:
        minus.append(value)
    else:
        plus.append(value)
minus.sort(reverse=True)
plus.sort()
ans = 0
current = 0
i = 0
j = 0

while i < len(minus) and j < len(plus):
    m = minus[i]
    m_dis = abs(m - current)
    p = plus[j]
    p_dis = abs(p - current)
    if m_dis <= p_dis:
        ans += m_dis
        current = m
        i += 1
    else:
        ans += p_dis
        current = p
        j += 1

remain_m = minus[i:]
remain_p = plus[j:]

if len(remain_m) > 0:
    for m in remain_m:
        m_dis = abs(m - current)
        current = m
        ans += m_dis
if len(remain_p) > 0:
    for p in remain_p:
        p_dis = abs(p - current)
        current = p
        ans += p_dis

print(ans)
