# que 13:
## Numbers ki list di hai. Kitne even hain ginno.
# Given: nums = [1, 4, 6, 7, 10, 3]

# step 1:   Restate:
# Numbers ki list di hai. Kitne even hain ginno.

# step 2:    ex: 2, 4, 6, 10 (2 ke table mai aale valeno.)

# step 3:   pseudocode:

# 1: nums ki list likhiye.
# 2: for mai n % 2 == 0:
# 3: print mai n print karo.

# step 4:

nums = [1, 4, 6, 7, 10, 3]
for n in nums:
 
 if n % 2 == 0:
  
  print(n)

# step 5:

# step  nums    n % 2
# s1     1        -
# if     1        1
# s2     4        1
# if     4        0
# s3     6        0
# if     6        0
# s4     7        0
# if     7        1
# s5     10       1
# if     10       0
# s6     3        0
# if     3        1
# print(4, 6, 8)