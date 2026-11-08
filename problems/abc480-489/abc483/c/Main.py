N, M = map(int, (input().split()))
# tokuten = [0 for i in range(N)]
# tokutens = []

second = [[] for _ in range(N)]
votes = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    votes[a] += 1
    second[a].append(b)

# 得票数1位と2位の候補者を求める
top1 = -1
top2 = -1

for i in range(N):
    if top1 == -1 or votes[i] > votes[top1]:
        top2 = top1
        top1 = i
    elif top2 == -1 or votes[i] > votes[top2]:
        top2 = i

# 候補者kが辞退する場合を順番に調べる
for k in range(N):
    # ① 辞退した候補者の票を第二希望に移す
    for b in second[k]:
        votes[b] += 1

    # ② 暫定当選者を決める
    if k == top1:
        winner = top2
    else:
        winner = top1

    # ③ 票が増えた候補者だけ確認する
    for b in second[k]:
        if votes[b] > votes[winner]:
            winner = b
        elif votes[b] == votes[winner] and b < winner:
            winner = b

    print(winner + 1)

    # ④ 増やした票を元に戻す
    for b in second[k]:
        votes[b] -= 1
