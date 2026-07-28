# que 27
## Ek number diya hai. Uske digits ka sum print karo (`while`).
# Given: n = 123   →  6 

# step 1:
# Ek number diya hai. Uske digits ka sum print karo (`while`).

# step 2:   ex:  3, 5, 6

# step 3:
# 1: num mai value likho.
# 2: sum = 0 do.
# 3: while mai num > 0 do.
# 4: digit = num % 10 do quki num ko 10 se reaminder chahiye.
# 5: sum += digit bhi bol sakte hai short mai.
# 6: num //= 10 bhi bol sakte hai short mai.
# 7: print mai sum do.

# step 4:

num = 123
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
    print(sum)

# step 5:  

# step      num     sum     digit       n //10
# s1        123      -       -            -
# s2        123      0       -            -
# d1        123      0       3            -
# s1        123      3       3            -
# n1        123      3       3            12
# d2        12       3       2            12
# s2        12       5       2            12
# n2        12       5       2            1
# d3        1        5       1            1
# s3        1        6       1            1
# n3        1        6       1            0
# print(3, 5, 6)   