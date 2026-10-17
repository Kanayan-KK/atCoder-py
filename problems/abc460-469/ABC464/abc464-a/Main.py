s = str(input())
e = 0
for w in s:
    if w == "E":
        e += 1

print("West" if len(s) - e > e else "East")
