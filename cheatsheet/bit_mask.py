# bit-mask: 1つの整数の各ビットを True / False として使う
mask = 0b1010
print(mask)  # 10
print(f"{mask:04b}")  # 1010（4桁の2進数）

# 基本のビット演算
left = 0b1100
right = 0b1010
print(f"{left & right:04b}")  # AND: 1000（両方が1）
print(f"{left | right:04b}")  # OR:  1110（どちらかが1）
print(f"{left ^ right:04b}")  # XOR: 0110（片方だけが1）
print(f"{left << 1:04b}")  # 左シフト: 11000（2倍）
print(f"{left >> 1:04b}")  # 右シフト: 0110（2で割った商）

# 下位4ビットだけを反転する
width = 4
print(f"{(~left) & ((1 << width) - 1):04b}")  # NOT: 0011

# i番目のビットを操作する（右端は0番目）
mask = 0
mask |= 1 << 1  # 1番目を立てる: 0010
mask |= 1 << 3  # 3番目を立てる: 1010
print(f"{mask:04b}")  # 1010
print(bool(mask & (1 << 3)))  # 3番目が立っているか: True

mask &= ~(1 << 1)  # 1番目を下ろす: 1000
print(f"{mask:04b}")  # 1000
mask ^= 1 << 2  # 2番目を反転する: 1100
print(f"{mask:04b}")  # 1100

# bit_count(): 立っているビットの個数を数える
print(mask.bit_count())  # 2

# 要素の選ぶ・選ばないを全列挙する（2 ** n通り）
items = ["A", "B", "C"]
for mask in range(1 << len(items)):
    selected = [item for i, item in enumerate(items) if mask & (1 << i)]
    print(f"{mask:03b}: {selected}")
# 000: []
# 001: ['A']
# 010: ['B']
# 011: ['A', 'B']
# 100: ['C']
# 101: ['A', 'C']
# 110: ['B', 'C']
# 111: ['A', 'B', 'C']

# 指定した集合の部分集合だけを列挙する
target = 0b1101
submask = target
while True:
    print(f"{submask:04b}")  # 1101, 1100, 1001, 1000, 0101, 0100, 0001, 0000
    if submask == 0:
        break
    submask = (submask - 1) & target
