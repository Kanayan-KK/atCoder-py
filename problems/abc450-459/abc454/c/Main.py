# 実行時エラーになった、おそらく再帰回数制限
# n, m = map(int, input().split())
# dictionary: dict[int, list[int]] = {}
# for i in range(m):
#     a, b = map(int, input().split())
#     if a in dictionary:
#         dictionary[a].append(b)
#     else:
#         dictionary[a] = [b]
# result = set()
# def get_item(item_id: int):
#     global result
#     if item_id in result:
#         return
#     result.add(item_id)

#     if item_id in dictionary:
#         item_ids = dictionary[item_id]
#         for id in item_ids:
#             get_item(id)
# get_item(1)
# print(len(result))

# スタック版
n, m = map(int, input().split())
dictionary: dict[int, list[int]] = {}
for _i in range(m):
    a, b = map(int, input().split())
    if a in dictionary:
        dictionary[a].append(b)
    else:
        dictionary[a] = [b]

result = set()
stack = [1]

while stack:
    item_id = stack.pop()
    if item_id in result:
        continue
    result.add(item_id)
    if item_id in dictionary:
        for id in dictionary[item_id]:
            stack.append(id)

print(len(result))