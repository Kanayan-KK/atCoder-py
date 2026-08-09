import heapq

# heapq: 最小値を何度も取り出したいときに使う
# 先頭の heap[0] が常に最小値になるが、配列全体は昇順とは限らない
min_heap = [5, 2, 8]
heapq.heapify(min_heap)  # 通常のlistを最小ヒープに変換
print(min_heap[0])  # 2（最小値を確認するだけ）

# heappush(): 値を追加して、最小値が先頭になる状態を保つ
heapq.heappush(min_heap, 1)
print(min_heap[0])  # 1

# heappop(): 先頭の最小値を取り出して削除する
smallest = heapq.heappop(min_heap)
print(smallest)  # 1
print(min_heap[0])  # 2（次の最小値）

# 小さい順にすべて取り出す
ordered = []
while min_heap:
    ordered.append(heapq.heappop(min_heap))
print(ordered)  # [2, 5, 8]

# 最大値を優先する場合は、符号を反転して保存する
max_heap = []
for number in [5, 2, 8]:
    heapq.heappush(max_heap, -number)
largest = -heapq.heappop(max_heap)
print(largest)  # 8

# tupleを入れると、先頭の値が小さい順に取り出される
# 優先度が同じ場合は、tupleの2番目以降で比較される
tasks = []
heapq.heappush(tasks, (2, "掃除"))
heapq.heappush(tasks, (1, "提出"))
heapq.heappush(tasks, (3, "買い物"))
priority, task = heapq.heappop(tasks)
print(priority, task)  # 1 提出

# nsmallest()、nlargest(): 小さい値・大きい値を必要な個数だけ取得する
scores = [70, 90, 60, 80, 100]
print(heapq.nsmallest(2, scores))  # [60, 70]
print(heapq.nlargest(2, scores))  # [100, 90]

# heappushpop(): 追加してから最小値を取り出す
top_three = [70, 80, 90]
heapq.heapify(top_three)
removed = heapq.heappushpop(top_three, 100)
print(removed)  # 70
print(sorted(top_three, reverse=True))  # [100, 90, 80]

# 計算量
# heapify(): O(N)
# heap[0]: O(1)
# heappush()、heappop(): O(log N)

# 使い分け
# 最小値・最大値を1回だけ求める: min()、max()
# 全要素を並べ替える: sorted()
# 最小値・最大値を何度も更新して取り出す: heapq
# 優先度順に処理する: (優先度, 値) のtupleをheapqに入れる
