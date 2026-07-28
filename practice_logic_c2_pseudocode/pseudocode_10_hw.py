# que 10:
## Total seconds diye hain. Kitne poore minutes aur bache hue seconds print karo.
# Given: total = 130   →  2 minutes 10 seconds


# step 1:
## Total seconds diye hain. Kitne poore minutes aur bache hue seconds print karo.

# step 2:    ex :   minute ke liye //, second ke liye %

# step 3:    pseudocode:

# 1: total  = 130 likhiye.
# 2: minute nikale total // 60 karke.
# 3: second nikale total % 60 karke. 
# 4: print minute and second likho.


# step 4: Traslate:

total = 130

minutes = total // 60
seconds = total % 60

print("Minute =", minutes)
print("Second=", seconds)

# step 5:

# step      total       minutes      seconds
# s1        130             -           -
# //        130             2           -
# %         130             2           10
# print(2)
# print(10)