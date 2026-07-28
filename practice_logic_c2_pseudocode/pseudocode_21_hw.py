# que 21:
## Ek list di hai. Sirf odd numbers ka sum print karo.
# Given: nums = [1, 2, 3, 4, 5, 6]

# step 1:
## Ek list di hai. Sirf odd numbers ka sum print karo.
 
# step 2:     ex : 1,3,5 = 9

# step 3: pseudocode:

# 1: num list bamao.
# 2: sum = 0 do.
# 3: num ki jagh hum n likh sakate hai.
# 4: if mai n % 2 0dd ke liye (!) symbol de = 0.
# 5: sum = sum + n kare.
# 6: print mai sum de.

# step 4:

nums =  [1, 2, 3, 4, 5, 6]

sum = 0
for n in nums:
     if n % 2 != 0:
        sum = sum + n
        print("sum of odd no.:", sum)

# step 5:


 # step    nums        sum  `   `
 # s1       1           -
 # s2       1           0
 # f-lp1    1           0
 # if       1           1
 # f-lp2    2           1
 # if       2           1
 # f-lp3    3           1
 # if       3           4
 # f-lp4    4           4
 # if       4           4
 # f-lp5    5           4
 # if       5           9
 # f-lp6    6           9
 # if       6           9
 # print(1, 4, 9)