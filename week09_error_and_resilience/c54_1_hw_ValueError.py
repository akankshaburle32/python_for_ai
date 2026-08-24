# c54:  que 1:
## Ek function `set_marks(m)` jo 0-100 ke bahar value par ValueError raise kare.

# step 1:
## Ek function `set_marks(m)` jo 0-100 ke bahar value par ValueError raise kare.

# step 2:

# step 3:

# 1: def mai fun lo usme m lo.
# 2: if mai m < 0 or m > 100.
# 3: raise mai ValueError mai error do kiska haito.
# 4: return m
# 5: print mai fun usme value.

# step 4:

def set_marks(m):
    if m < 0 or m > 100:
        raise ValueError("Marks must be between 0 and 100")
    return m

print(set_marks(80))

# step 5:

"""
80

"""