s = str(input())
array = []
last_i = len(s) - 1
for i,word in enumerate(s):
    if i != last_i:
        array.append(word + "o")
    else:
        array.append(word)
print("".join(array))