# c39:      que 2:

# `filter` + lambda se `[3,8,1,9,4]` mein se sirf 5 se bade rakho.

# step 1:
## `filter` + lambda se `[3,8,1,9,4]` mein se sirf 5 se bade rakho.

# step 2: ex:  [8, 9, 4, 7] = [7, 8, 9]

# step 3:

# 1: list lo.
# 2: var mai = list mai filter mai lambda parameter : parameter > 5, list.
# 3: print mai var.

# step 4:

nums = [3, 8, 1, 9, 4]

high_number = list(filter(lambda x: x > 5, nums))

print(high_number)

# step 5:

"""
[8, 9]

"""