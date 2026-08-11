import math

# /は通常の割り算、//は小数部分を切り下げた商を求める
print(7 / 3)  # 2.333...: 結果はfloat
print(7 // 3)  # 2: 結果はint

# //は負の無限大方向へ切り下げる。0方向への切り捨てではない
print(-7 // 3)  # -3
print(int(-7 / 3))  # -2: int()は0方向へ切り捨てる

# 商と余りを同時に使うならdivmod()を選ぶ
quotient, remainder = divmod(7, 3)
print(quotient, remainder)  # 2 1

# 正の整数aを正の整数b個ずつに分けるときの必要個数（切り上げ除算）
a, b = 7, 3
print((a + b - 1) // b)  # 3

# 絶対値を求める
print(abs(-10))  # 10
print(abs(3 - 8))  # 2つの値の差: 5

# math.fabs()でも求められるが、結果は常にfloatになる
print(math.fabs(-10))  # 10.0

# 小数を整数方向に丸める
print(math.floor(3.8))  # 切り下げ: 3
print(math.ceil(3.2))  # 切り上げ: 4

# 平方根を求める
print(math.sqrt(10))  # 小数の平方根: 3.162...
print(math.isqrt(10))  # 整数の平方根を切り捨て: 3

# 最大公約数と最小公倍数
print(math.gcd(12, 18))  # 6
print(math.lcm(12, 18))  # 36

# 階乗、組合せ、順列
print(math.factorial(5))  # 5! = 120
print(math.comb(5, 2))  # 5個から2個を選ぶ: 10
print(math.perm(5, 2))  # 5個から2個を選んで並べる: 20

# 配列内のすべての値を掛ける
print(math.prod([2, 3, 4]))  # 24

# 対数を求める
print(math.log2(8))  # 3.0
print(math.log10(1000))  # 3.0

# 円周率と無限大
print(math.pi)  # 3.141592...
print(100 < math.inf)  # True

# 小数は誤差を考慮して比較する
print(0.1 + 0.2 == 0.3)  # False
print(math.isclose(0.1 + 0.2, 0.3))  # True
