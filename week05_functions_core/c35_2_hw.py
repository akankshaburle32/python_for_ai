# c35:      que 2:
## Ek function `is_even(n)` jo True/False return kare; 5 numbers par test karo.

# step 1:
# Ek function `is_even(n)` jo True/False return kare; 5 numbers par test karo.

# step 2:  ex.  2, 4, 6, 8, jo 2 se divide hota hai.

# step 3:

# 1: def mai fun mai (n) . ise karke even(n)
# 2: return mai n % 2 == 0
# 3: for mai p ki dict mai no. do.
# 4: print mai p, even(p)


# step 4:

def even(n):
    return n % 2 == 0
for p in [8, 7, 6, 7, 3, 0, 6, 7, 1, 6]:

    print(p, even(p))


# step 5:

# 8 True
# 7 False
# 6 True
# 7 True
# 3 False
# 0 True
# 6 True
# 7 False
# 1 False
# 6 True