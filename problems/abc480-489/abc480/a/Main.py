first_strings = str(input())
second_strings = str(input())

if first_strings == "AD" or first_strings == "DA":
    print("Yes")
elif second_strings == "AD" or second_strings == "DA":
    print("Yes")
# AX
# DX
elif first_strings[0] == "A" and second_strings[0] == "D":
    print("Yes")

# DX
# AX
elif first_strings[0] == "D" and second_strings[0] == "A":
    print("Yes")

# XA
# XD
elif first_strings[1] == "A" and second_strings[1] == "D":
    print("Yes")

# XD
# XA
elif first_strings[1] == "D" and second_strings[1] == "A":
    print("Yes")
else:
    print("No")
