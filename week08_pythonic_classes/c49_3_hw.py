# c49:  que 3:
## Circle class mein diameter property (2 * radius) add karo.

# step 1:
## Circle class mein diameter property (2 * radius) add karo.

# step 2:

# step 3:

# 1: Circle ka class lo.
# 2: def __init__ lo usme self or radius lo.
# 3: attribute lo.
# 4: @property lo.
# 5: def mai diameter method lo.
# 6: return mai formula do.
# 7: print mai C.diameter lo.

# step 4:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

C = Circle(7)
print(C.diameter) 

# Step 5: 

"""
14

"""