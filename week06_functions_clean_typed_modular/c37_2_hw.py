# c37:  que 2:
# Recursion se factorial(6) nikalo.

# step 1:
# Recursion se factorial(6) nikalo.

# step 2:  ex:  2* 1 >> 2

# step 3:

# 1: def mai fun banaye or usme n naam ka parameter do (n).
# 2: if mai n equal to equal to 1 do.
# 3: return mai 1 do. 
# 4: return mai n*factorial (n-1) ye diya to vo vese solve karke return karega.
# 5: print mai fun or usme no. do. 

# step 4:

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1) 

print(factorial(6))    


# step 5:

# 6 * factorial >> 6* 5* 4* 3* 2* 1   = 30 > 120 > 360 > 720 > 720
# 720