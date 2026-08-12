# c44:  que 2:
## Ek list mein alag shapes daalo aur loop se sabka area print karo.

# step 1:
## Ek list mein alag shapes daalo aur loop se sabka area print karo.

# step 2:

# step 3:

# 1: class mai parent lo.
# 2: def __init__ method lo or usme common word lo or 2 para. attribute lo.
# 3: shapes mai list lo alag-alag shape ki. 
# 4: for mai shepes ki jagah hum shape likh sakte hai.
# 5: print mai name ka area nikolo ise print mai do.

# step 4: 

class Shape:
    def __init__(self, name, area):
        self.name = name
        self.area = area

Shapes = [
            Shape("Circle", 78.5),
            Shape("Square", 16),
            Shape("Rectangle", 18)
        ]        

for Shape in Shapes:
    print(Shape.name, "area =", Shape.area)

# step 5:

"""
Circle area = 78.5
Square area = 16
Rectangle = 18

"""