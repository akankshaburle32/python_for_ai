# que 20:
##  Ek list di hai. 10 se bade kitne numbers hain ginno.
# Given: nums = [5, 12, 8, 20, 10, 15]

# step 1:
# Ek list di hai. 10 se bade kitne numbers hain ginno.

# step 2:  ex :  i > 10

# step 3:

# 1: num ki list likho.
# 2: count = 0  count mai likho.
# 3: num ki jagh hum i lih sahkte hai.
# 4: if mai i greater than 10 likho.
# 5: count = count + 1
# 6: print mai count likho.

# step 4:

num = [5, 12, 8, 20, 10, 15] 

count = 0
for i in num:
  if i > 10:
    count = count + 1

    print(count)

# step 5:

# step    num     count    
# s1        5       -
# s2        5       0
# f-lp1     5       0
# if        5       0
# f-lp2     12      0   
# if        12      1
# f-lp3     8       1
# if        8       1
# f-lp4     20      1
# if        20      2
# f-lp5     10      2
# if        10      2
# f-lp6     15      2
# if        15      3
# print(1, 2, 3) 