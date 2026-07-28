# que 23:
## Ek number `n` diya hai. Uska factorial print karo.
# Given: n = 5   →  120


# step 1: 
# Ek number `n` diya hai. Uska factorial print karo.

# step 2:   ex :    1 x 2 x 3 x 4 x 5 = 120

# step 4:   psedocode:

# 1: num ki value likhiye.
# 2: fact ki value 1 do.
# 3: for mai hum range mai 1, n + 1 likh sakte hai.
# 4: fact mai hum fact * p likh sakte hai.
# 5: print mai fact likhiye.

# step 4:


num = 5
fact = 1

for p in range(1, num + 1):
    fact = fact * p
    print(fact)

# step 5:

# step      num     fact
# s1        5         -
# s2        5         1
# f-lp1     1         1
# f-lp1     1         1
# f-lp2     2         1
# f-lp2     2         2
# f-lp3     3         2
# f-lp3     3         6
# f-lp4     4         6
# f-lp4     4         24
# f-lp5     5         24
# f-lp6     5         120
# f-lp6     5         120
# print(1, 2, 6, 24, 120)