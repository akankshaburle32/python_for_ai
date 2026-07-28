# que 19:
## Ek number `n` diya hai. 1 se 10 tak uska table print karo.
# Given: n = 7   →  7 x 1 = 7 ... 7 x 10 = 70

# step 1:
# Ek number `n` diya hai. 1 se 10 tak uska table print karo.

# step 2:  ex:   7 x 1 = 7 ... 7 x 10 = 70

# step 3:

# 1: ek no likho.
# 2: for mai range dalo 1, 11 karke.
# 3: print mai num * t likho.

# step 4:

num = 7
for t in range(1, 11):
    print(num * t)


# step 5:

# step    num      range    num * t
# s1       7        -          -
# f-lp1    7        1          -
# f-lp1    7        1          7
# f-lp2    7        2          14
# f-lp3    7        3          21
# f-lp4    7        4          28
# f-lp5    7        5          35
# f-lp6    7        6          42
# f-lp7    7        7          49
# f-lp8    7        8          56
# f-lp9    7        9          63
# f-lp10   7        10         70
