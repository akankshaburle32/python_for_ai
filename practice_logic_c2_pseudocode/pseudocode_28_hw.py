# que 28:
## Ek number diya hai. Ulta print karo (`while`).
# Given: n = 123   →  321

# step 1:
# Ek number diya hai. Ulta print karo (`while`).

# step 2:  ex:

# step 3:
# 1: num ki value do.
# 2: reverse = 0 do.
# 3: while mai num > 0. lo
# 4: digit = num % 10 yahi karke reamainder aayga kam.
# 5: reverse function deneke bad hi no. revaerse ho jayga.
# 6: num = num // 10.
# 7: print mai reverse do. 

# step 4:

num = 123
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
    print(reverse)


# step 5:

#  step     num     reverse     digit                      £££ reverse 
#  s1       123         -         -                            
#  s1       123         0         -
#  d1       123         0         3
#  r1       123         3         3                             0 x 10 + 3 = 3
#  n2       12          3         3
#  d2       12          3         2
#  r2       12          32        2                             3 x 10 + 2 = 32  
#  n3       1           32        2
#  d3       1           32        1
#  r3       1           321       1                             32 x 10 + 1 = 321
# print(321)              