# que 36:
## Duplicates wali list di hai. Kitni unique values hain print karo (`set`).
# Given: nums = [1, 2, 2, 3, 3, 3, 4]

# step 1:
## Duplicates wali list di hai. Kitni unique values hain print karo (`set`).

# step 2:

# step 3:

# 1: nums mai dict do.
# 2: unique var lo usme set(nums) do.
# 3: print mai len(unique) lo.

# step 4:

nums = [1, 2, 2, 3, 3, 3, 4]
unique = set(nums)

print(len(unique))

# step 5:

# step     nums                      unique         len(umique)  
# 1    [1, 2, 2, 3, 3, 3, 4]           -                  -
# 2    [1, 2, 2, 3, 3, 3, 4]         [1, 2, 3, 4]         -
# 3    [1, 2, 2, 3, 3, 3, 4]         [1, 2, 3, 4]         4

# print(4)