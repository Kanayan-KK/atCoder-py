from typing import TypeAlias

# 型ヒント: 変数や関数が扱う値の型を明示する
count: int = 3
average: float = 2.5
name: str = "Alice"
is_valid: bool = True
print(count, average, name, is_valid)

# コレクションは要素の型も指定する
scores: list[int] = [80, 65, 90]
point: tuple[int, int] = (3, 5)
visited: set[int] = {1, 2, 3}
prices: dict[str, int] = {"apple": 120, "orange": 100}
grid: list[list[int]] = [[1, 2], [3, 4]]
print(scores, point, visited, prices, grid)


# 引数の型は「名前: 型」、戻り値の型は「-> 型」で指定する
def total(values: list[int]) -> int:
    return sum(values)


print(total(scores))  # 235


# 値がない可能性は「型 | None」で表す
def find_index(values: list[int], target: int) -> int | None:
    for index, value in enumerate(values):
        if value == target:
            return index
    return None


print(find_index(scores, 65))  # 1
print(find_index(scores, 100))  # None

# 複数の型を受け付ける場合は「|」でつなぐ
identifier: int | str = "A-10"
print(identifier)

# 長い型や繰り返し使う型には別名を付ける
UserId: TypeAlias = int
Coordinate: TypeAlias = tuple[int, int]
AdjacencyList: TypeAlias = list[list[int]]

user_id: UserId = 1001
start: Coordinate = (0, 0)
graph: AdjacencyList = [[1, 2], [0], [0]]
print(user_id, start, graph)

# 型ヒントは実行時に値を変換しない
number_text: str = "123"
number: int = int(number_text)
print(type(number_text))  # <class 'str'>
print(type(number))  # <class 'int'>
print(isinstance(number, int))  # True

# 数値を文字列に変換する
integer: int = 123
integer_text: str = str(integer)
print(integer_text)  # 123
print(type(integer_text))  # <class 'str'>

# 整数のlistは各要素をstrに変換してからjoin()で連結する
numbers: list[int] = [1, 2, 3, 4, 5]
space_separated: str = " ".join(map(str, numbers))
print(space_separated)  # 1 2 3 4 5

# 区切り文字を変える場合
comma_separated: str = ",".join(map(str, numbers))
print(comma_separated)  # 1,2,3,4,5

# 使い分け
# 変数の型を明示: variable: int = 0
# listなどの要素型を明示: list[int]
# 値がない可能性を明示: int | None
# 複数の型を許可: int | str
# 複雑な型を再利用: TypeAlias
# 実行時に型を確認: isinstance(value, type)
# 1つの数値を文字列化: str(number)
# 数値のlistを区切って文字列化: separator.join(map(str, numbers))
