# c39:      que 3:

# Words ki list `["hi","hello","hey","welcome"]` mein se sirf 4+ letter waale `filter` se rakho.

# step 1:
## Words ki list `["hi","hello","hey","welcome"]` mein se sirf 4+ letter waale `filter` se rakho.

# step 2:     ["rose", "sunflower", "mogra", "lotus"] = len(x) < 4 <<<< ['rose']

# step 3:

# 1: list lo.
# 2: var = list mai filter mai lambda parameter mai len(parameter) > 4, list.
# 3: print mai var.

# step 4:

words = ["hi","hello","hey","welcome"]

count_words = list(filter(lambda x: len(x) > 4, words))

print(count_words)

# step 5:

"""
['hello', 'welcome']

"""