# que 26:
## Ek number diya hai. Usme kitne digits hain ginno (`while` + `// 10`).
# Given: n = 4592   →  4


# step 1:
# Ek number diya hai. Usme kitne digits hain ginno (`while` + `// 10`).

# step 2:    ex:  4592 = 4

# step 3: 

# 1: num mai hum value likh sakte hai.
# 2: count = 0 de sakte hai quvki abhi tak count value nhi hai isiliye.
# 3: while mai hum num > 0 de sakte hai.
# 4: count = count + 1 de sakte hai quvki count ki badegi.
# 5: num = num // 10 bhi likh sakte hai.
# 6: print mai hum count likh sakte hai.

# step 4:

num =  4592

count = 0

while num > 0:
    count = count + 1
    num = num // 10

    print(count)

# step 5:

# step      num     count   //
# s1        4592      -     -
# s2        4592      0     -
# w1        4592      0     -
# c1        4592      1     4592
# n1        4592      1     459
# c2        4592      2     459
# n1        4592      2     45
# c3        4592      3     45
# n3        4592      3     4
# c4        4592      4     4
# print(1, 2, 3, 4)