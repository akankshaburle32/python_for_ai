# que 15:
## Ek word diya hai. Usme vowels ginno.
# Given: word = "education"

# step 1:   
# Ek word diya hai. Usme vowels ginno.

# step 2:  ex:  bee = 2

# step 3:

# 1: word ka name do education.
# 2: count = 0
# 3: if mai word digiye education.
# 4: for mai letter do word karke.
# 5 if mai vowel dijiye.
# 6: phir count + 1 karo.
# 7: phir print karo.


# step 4:

word = "education"
count = 0
if word in ["education"]:
    for letter in word:
        if letter in "aeiou":
            count = count + 1
            print (count)



# step 5:

# step    word              count
# s1      education           -
# s2      education           0
# f-lp1      e                0
# if         e                1
# f-lp2      d                1
# if         d                1
# f-lp3      u                1
# if         u                2
# f-lp4      c                2
# if         c                2
# f-lp5      a                2
# if         a                3
# f-lp6      t                3
# if         t                3
# f-lp7      i                3
# if         i                4
# f-lp8      o                4
# if         o                5
# f-lp9      n                5
# if         n                5
print(5)