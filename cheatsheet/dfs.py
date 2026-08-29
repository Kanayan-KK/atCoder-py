import sys

# DFS（深さ優先探索）: 行き止まりまで進んでから戻る探索
graph = [
    [1, 2],
    [0, 3],
    [0, 4],
    [1],
    [2],
]

# 再帰版: 処理の流れを書きやすいが、深い探索では再帰上限に注意する
sys.setrecursionlimit(10**6)


def recursive_dfs(start: int) -> list[int]:
    visited = [False] * len(graph)
    order = []

    def visit(node: int) -> None:
        visited[node] = True
        order.append(node)
        for next_node in graph[node]:
            if not visited[next_node]:
                visit(next_node)

    visit(start)
    return order


print(recursive_dfs(0))  # [0, 1, 3, 2, 4]


# スタック版: 再帰上限を気にせず探索できる
def iterative_dfs(start: int) -> list[int]:
    visited = [False] * len(graph)
    visited[start] = True
    stack = [start]
    order = []

    while stack:
        node = stack.pop()  # 末尾から取り出す（LIFO）
        order.append(node)

        # 逆順に積むと、再帰版と同じ順番で探索できる
        for next_node in reversed(graph[node]):
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)

    return order


print(iterative_dfs(0))  # [0, 1, 3, 2, 4]

# 非連結グラフでは、未訪問の頂点ごとにDFSを始める
disconnected_graph = [[1], [0], [3], [2], []]
component_visited = [False] * len(disconnected_graph)
component_count = 0

for component_start in range(len(disconnected_graph)):
    if component_visited[component_start]:
        continue

    component_count += 1
    component_visited[component_start] = True
    component_stack = [component_start]
    while component_stack:
        component_node = component_stack.pop()
        for component_next_node in disconnected_graph[component_node]:
            if not component_visited[component_next_node]:
                component_visited[component_next_node] = True
                component_stack.append(component_next_node)

print(component_count)  # 3

# グリッドでは上下左右の移動先が範囲内か確認する
grid = [
    "S..#",
    ".#.#",
    "...G",
]
height = len(grid)
width = len(grid[0])
start_cell: tuple[int, int] = (0, 0)
goal_cell: tuple[int, int] = (2, 3)
visited_cells: set[tuple[int, int]] = {start_cell}
cell_stack: list[tuple[int, int]] = [start_cell]

while cell_stack:
    row, column = cell_stack.pop()
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        next_row = row + dr
        next_column = column + dc
        next_cell = (next_row, next_column)
        if not (0 <= next_row < height and 0 <= next_column < width):
            continue
        if grid[next_row][next_column] == "#" or next_cell in visited_cells:
            continue
        visited_cells.add(next_cell)
        cell_stack.append(next_cell)

print(goal_cell in visited_cells)  # True
