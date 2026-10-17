N=int(input())
A=list(map(int,input().split()))
c100,c10,c1=0,0,0
for a in A:
  x=(-a)%1000
  c100+=x//100
  c10+=x//10%10
  c1+=x%10
print(c1,c10,c100)

# n = int(input())
# amounts = list(map(int, input().split()))
# sen_in_w = 10 ^ 100
# hyaku_in_w = 0
# juu_in_w = 0
# ichi_in_w = 0


# for amount in amounts:
#     sen_c = amount // 1000
#     sen_in_w -= sen_c
#     amount -= 1000 * sen_c

#     hyaku_c = amount // 100
#     if hyaku_c > hyaku_in_w:
#         sen_in_w -= 1
#         otsuri =  1000 - amount
#         hyaku_otsuri = otsuri // 100




#         continue
#     else:
#         hyaku -= hyaku_c

#     juu_c = (amount - 1000 * sen_c - 100 * hyaku_c) // 10
#     if juu_c > juu:
#         hyaku += juu_c + 1
#         continue
#     else:
#         juu -= juu_c

#     ichi_c = (amount - 1000 * sen_c - 100 * hyaku_c - 10 * juu_c) // 1
#     if ichi_c > ichi:
#         ichi += ichi_c + 1
#         continue
#     else:
#         ichi -= ichi_c

# print(" ".join(map(str, [hyaku, juu, ichi])))
