# c35:  que 2:
# make_adder(n) closure banao jo n add kare; add5 = make_adder(5) test karo.

# step 1:
# make_adder(n) closure banao jo n add kare; add5 = make_adder(5) test karo.

# step 2:  5 + 2 = 7, 5 + 4 = 9

# step 3:

# 1: def mai fun lo or usme ek parameter do.
# 2: def mai or ek fun lo or usme parameter do.
# 3: return in dono ki sum karo (x + n).
# 4: return mai add likho.
# 5: qu mai dusra ek fun hai vo do.
# 6: print mai fun or ek value do. ese 2 baar karo.

# step 4: 

def make_adder(n):
    def add(x):
        return x + n
    return add

add5 = make_adder(5)
print(add5(16))
print(add5(15))

# step 5:

# 5 + 16 = 21
# 5 + 15 = 20