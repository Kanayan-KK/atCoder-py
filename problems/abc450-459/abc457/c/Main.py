n, k = map(int, input().split())
array = [[] for _i in range(n)]
for _i in range(n):
    temp = list(map(int, input().split()))
    array[_i] = [temp[0], temp[1:]]

c_array = list(map(int, input().split()))

for _i in range(n):
    if k - (array[_i][0] * c_array[_i]) > 0:
        k -= array[_i][0] * c_array[_i]
    else:
        amari = k % array[_i][0]
        print(array[_i][1][amari - 1])
        break
