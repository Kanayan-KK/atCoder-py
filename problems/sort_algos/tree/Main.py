# TreeSort(二部探索木)(https://en.wikipedia.org/wiki/Tree_sort)


class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


# 挿入
def insert(root: Node | None, value: int):
    # root が空なら新しい Node を返す
    if root is None:
        return Node(value)

    # value が root.value より小さいなら左へ
    # それ以外なら右へ
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# 巡回
def inorder(root: Node | None, result: list[int]):
    # root が None なら終了
    if root is None:
        return

    # 左を巡回
    inorder(root.left, result)

    # 自分の値を追加
    result.append(root.value)

    # 右を巡回
    inorder(root.right, result)

    return result


def tree_sort(array: list[int]):
    root = None

    # array の値を順番に insert
    for i in range(len(array)):
        root = insert(root, array[i])

    result = []

    # inorder で result に格納
    inorder(root, result)

    return result


numbers = list(map(int, input().split()))
result = tree_sort(numbers)
print(" ".join(map(str, result)))
