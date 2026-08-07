# c39:      que 1:

# `map` + lambda se `[1,2,3,4]` ke har number ka cube banao.

# step 1:
## `map` + lambda se `[1,2,3,4]` ke har number ka cube banao.

# step 2:   ex. : x ** 3 = x=(2) >> 8

# step 3:

# 1: list lo.
# 2: ek var = list mai map mai labda parameter mai : parameter ** 3, list  
# 3: print mai var.

# step 4:

nums = [1, 2, 3, 4]

cube = list(map(lambda x: x ** 3, nums))

print(cube)

# step 5:

"""
[1, 8, 27, 64]

"""