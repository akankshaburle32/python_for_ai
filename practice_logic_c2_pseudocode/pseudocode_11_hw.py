# que 11:
## Ek number `i. 1 se `n` tak sabka sum print karo.n` diya hai.
# Given: n = 5   →  1+2+3+4+5 = 15

# step 1:    Restate:
# Ek number `i. 1 se `n` tak sabka sum print karo.n` diya hai.

# step 2:   ex: 1 + 2 = 3 + 3 = 6

# step 3:   pseudocode:

# 1: num mai 5  likhe.
# 2: total = 0.
# 3: for mai range 1, n+ 1.
# 4: total + n.
# 5: print mai total.

# step 4:  Traslate

num = 5
total = 0
for n in range(1, num+ 1):
    total = total + n
    print(total)


# step 5:

# step      num   total   n
# s1         5      -     -
# s2         5      0     -
# f-lp1      5      0     1
# f-lp1      5      1     1
# f-lp2      5      1     2
# f-lp2      5      3     2
# f-lp3      5      3     3
# f-lp3      5      6     3
# f-lp4      5      6     4
# f-lp4      5      10    4
# f-lp5      5      10    5
# f-lp6      5      15    5
# print(1)
# print(3)
# print(6)
# print(10)
# print(15)      