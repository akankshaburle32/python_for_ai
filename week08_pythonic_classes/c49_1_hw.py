# c49:  que 1:
## Square class mein area property banao.

# step 1:
## Square class mein area property banao.

# step 2: 

# step 3:

# 1: Square ka class lo.
# 2: def __init__ method lo.
# 3: or atrribute lo.
# 4: @property lo. 
# 5: def mai area method lo.
# 6: return mai arrtibute * attribute lo.
# 7: S = Square ki jagh de sakte hai.
# 8:print mai S.area do

# step 4:

class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side * self.side

S = Square(8)
print(S.area)   

# step 5:

"""
64

"""