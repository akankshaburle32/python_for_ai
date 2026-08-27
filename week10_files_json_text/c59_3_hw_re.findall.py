# c59:  que 3:
## Ek text se saare hashtags (`#word`) nikaalo.

# step 1:
## Ek text se saare hashtags (`#word`) nikaalo.

# step 2:

# step 3:

# 1: import mai re lo.
# 2: text # ke word lo.
# 3: var lo usme re.findall(r"#\w+", text)
# 4: print mai var do.

# step 4:

import re

text = "#Python, #Hello, #Student, #Sir."

hashtags = re.findall(r"#\w+", text)

print(hashtags)

# step 5:

"""
['#Python', 'Hello', '#Student', 'Sir']

"""