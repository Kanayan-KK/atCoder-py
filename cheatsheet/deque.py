from collections import deque

# queue: 先に追加した要素から取り出す（FIFO）
queue = deque(["A", "B"])
queue.append("C")  # 右端（末尾）に追加
print(queue.popleft())  # A（左端の最初に入れた要素）
print(queue)  # deque(['B', 'C'])

# deque.pop(): 右端から取り出すためFIFOにはならない
print(queue.pop())  # C
print(queue)  # deque(['B'])

# 先頭や末尾で要素を追加、削除するときに使う
