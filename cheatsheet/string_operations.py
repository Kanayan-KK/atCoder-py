# 文字列の位置は0から数える
text = "apple banana apple"

# find(): 最初に一致した文字列の開始位置を返す
first_index = text.find("apple")
print(first_index)  # 0
print(text.find("banana"))  # 6

# 見つからない場合は-1を返す
missing_index = text.find("orange")
print(missing_index)  # -1

# 第2引数以降で検索する範囲を指定できる
second_index = text.find("apple", first_index + 1)
print(second_index)  # 13
print(text.find("apple", 1, 12))  # -1（位置1以上12未満を検索）

# rfind(): 最後に一致した文字列の開始位置を返す
print(text.rfind("apple"))  # 13

# in: 位置が不要で、含まれているかだけを調べる
print("banana" in text)  # True
print("orange" not in text)  # True

# index(): find()と似ているが、見つからない場合はValueErrorになる
print(text.index("banana"))  # 6
# print(text.index("orange"))  # ValueError

# count(): 重ならない一致の個数を数える
print(text.count("apple"))  # 2
print("aaaa".count("aa"))  # 2

# すべての一致位置を取得する関数（重なる一致にも対応）
def find_all_indices(source: str, target: str) -> list[int]:
    if target == "":
        return []

    indices = []
    start = 0

    # 前回の開始位置から1文字進めて、次の一致を検索する
    while True:
        index = source.find(target, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1

    return indices


print(find_all_indices("banana", "ana"))  # [1, 3]

# startswith()・endswith(): 先頭または末尾の一致を調べる
filename = "answer.py"
print(filename.startswith("answer"))  # True
print(filename.endswith(".py"))  # True

# replace(): 一致した文字列を置き換える
message = "red blue red"
print(message.replace("red", "green"))  # green blue green
print(message.replace("red", "green", 1))  # green blue red

# split(): 区切り文字で分割し、join(): 文字列を連結する
csv_text = "red,blue,green"
colors = csv_text.split(",")
print(colors)  # ['red', 'blue', 'green']
print("-".join(colors))  # red-blue-green

# strip(): 先頭と末尾の余分な空白を取り除く（Trimに相当）
input_text = " \t hello world \n"
print(input_text.strip())  # hello world

# lstrip()は先頭だけ、rstrip()は末尾だけを取り除く
print(input_text.lstrip())  # 末尾側の空白と改行は残る
print(input_text.rstrip())  # 先頭側の空白とタブは残る

# 文字列の途中にある空白は取り除かない
spaced_text = "  hello   world  "
print(spaced_text.strip())  # hello   world

# スライス: 開始位置以上、終了位置未満の部分文字列を取得する
word = "Python"
print(word[0])  # P
print(word[1:4])  # yth
print(word[::-1])  # nohtyP

# 大文字・小文字の変換と判定
mixed = "PyThOn"
print(mixed.lower())  # python
print(mixed.upper())  # PYTHON
print(mixed.lower() == "python")  # True

# 文字の種類を判別する（1文字だけでなく、全ての文字を調べる）
print("123".isdigit())  # True: 全て数字
print("12a".isdigit())  # False
print("abc".isalpha())  # True: 全て英字などの文字
print("abc123".isalnum())  # True: 全て文字または数字
print(" \t\n".isspace())  # True: 全て空白文字
print("ABC".isupper())  # True: 大文字のある文字が全て大文字
print("abc".islower())  # True: 小文字のある文字が全て小文字
print("abc123".isascii())  # True: 全てASCII文字

# 空文字では、上記の判定はisascii()を除いてFalseになる
print("".isdigit())  # False
print("".isascii())  # True

# isdigit()は符号や小数点を数字とは判定しない
print("-123".isdigit())  # False
print("1.5".isdigit())  # False
print("-123".lstrip("+-").isdigit())  # True: 先頭の符号を除いて判定

# 0～9だけに限定したい場合（isdigit()は一部のUnicode数字もTrue）
print("１２３".isdigit())  # True: 全角数字
print("１２３".isascii() and "１２３".isdigit())  # False
print("123".isascii() and "123".isdigit())  # True

# 使い分け
# 最初の位置を知る: find()
# 最後の位置を知る: rfind()
# 存在だけを知る: in
# 見つからない場合を例外にしたい: index()
# すべての位置を知る: find()を開始位置を変えながら繰り返す
# 数字だけか調べる: isdigit()
# 文字だけか調べる: isalpha()
# 文字または数字だけか調べる: isalnum()
# 半角の0～9だけか調べる: isascii() and isdigit()
