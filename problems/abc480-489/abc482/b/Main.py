yoko: list[str] = []
# tate: list[str] = []

bingo_need = 5
for _i in range(5):
    yoko_str = input()
    bingo_need = min(bingo_need, 5 - yoko_str.count("o"))
    yoko.append(yoko_str)

for i in range(5):
    tate_str = ""
    for str in yoko:
        tate_str += str[i]
    bingo_need = min(bingo_need, 5 - tate_str.count("o"))

left_to_right_str = ""
right_to_left_str = ""
for i in range(5):
    left_to_right_str += yoko[i][i]
    right_to_left_str += yoko[4 - i][4 - i]

bingo_need = min(bingo_need, 5 - left_to_right_str.count("o"))
bingo_need = min(bingo_need, 5 - right_to_left_str.count("o"))

print(bingo_need)
