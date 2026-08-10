# dict（辞書）: キーと値を対応付けて管理する連想配列
scores = {"Alice": 80, "Bob": 65}

# キーを指定して値を取得する
print(scores["Alice"])  # 80
# print(scores["Carol"])  # 存在しないキーはKeyError
print(scores.get("Carol"))  # None
print(scores.get("Carol", 0))  # 0（存在しない場合の既定値）

# キーの存在を確認する
print("Bob" in scores)  # True
print("Carol" not in scores)  # True

# 新しい要素を追加し、既存の値を更新する
scores["Carol"] = 90
scores["Bob"] = 70
print(scores)  # {'Alice': 80, 'Bob': 70, 'Carol': 90}

# キー、値、キーと値の組を順番に取り出す
for name in scores:
    print(name)

for score in scores.values():
    print(score)

for name, score in scores.items():
    print(name, score)

# 要素を削除する
removed_score = scores.pop("Bob")
print(removed_score)  # 70
print(scores.pop("Dave", 0))  # 0（存在しなくてもKeyErrorにならない）
del scores["Alice"]
print(scores)  # {'Carol': 90}

# get(): 出現回数を数える
counts: dict[str, int] = {}
for character in "banana":
    counts[character] = counts.get(character, 0) + 1
print(counts)  # {'b': 1, 'a': 3, 'n': 2}

# setdefault(): キーがなければ初期値を追加してグループ分けする
groups: dict[int, list[str]] = {}
for word in ["cat", "apple", "dog"]:
    groups.setdefault(len(word), []).append(word)
print(groups)  # {3: ['cat', 'dog'], 5: ['apple']}

# 辞書内包表記で新しいdictを作る
squares = {number: number**2 for number in range(1, 4)}
print(squares)  # {1: 1, 2: 4, 3: 9}

# 使い分け
# 必ず存在するキーを取得: dictionary[key]
# 存在しない可能性があるキーを取得: dictionary.get(key, default)
# キーの有無だけを確認: key in dictionary
# キーがなければ初期値を作る: dictionary.setdefault(key, default)
