# c42:      que 3:
## Ek `Password` class with `_password` aur ek `check(guess)` method jo True/False de.

# step 1: 
# Ek `Password` class with `_password` aur ek `check(guess)` method jo True/False de.

# step 2:  p.check("Chaku@123") = False

# step 3:
# 1: class mai password class lo. 
# 2: def mai __inti__ mai self or ek parameter do.
# 3: def mai check lo usme self or ek parameter do.
# 4: return guess == self.password do.
# 5: passord do konsa bhi.
# 6: print mai class.check("or isme password do pahile ek wrong password do. or ek sahi password. do") ise 2 baar kar lo.

# step 4: 

class Password:
    def __init__(self, password):
        self._password = password
    def check(self, guess):
        return guess == self._password
p = Password("akanksha@123")
print(p.check("wrong"))      
print(p.check("akanksha@123"))  

# step 5:

"""
False
True

"""