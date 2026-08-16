# c42:      que 2:
## Ek `Temperature` class banao with `_celsius`; ek method `set_celsius` jo -273 se kam value reject kare.

# step 1:
# Ek `Temperature` class banao with `_celsius`; ek method `set_celsius` jo -273 se kam value reject kare.

# step 2:

# step 3:

# 1: Temperature ka class banao.
# 2: def mai __init__ method lo. self._celcius = 0 lo.
# 3: def mai set_celsius ki method do. if mai c < -273 lo else mai attribute lo.
# 4: print karo value dekar.

# step 4: 

class Temperature:
    def __init__(self):
        self._celsius = 0

    def set_celsius(self, c):
        if c < -273:
            print("Invalid")

        else:
            self._celsius = c    

T = Temperature()

print("=====================")
T.set_celsius(89)
T.set_celsius(-300)
print("=====================")

print(T._celsius)
print("=====================")

# step 5:

"""
====================
Invalid
===================
89
===================
"""