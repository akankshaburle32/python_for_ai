# c41:  que 3:
## Ek `Circle` class with `radius` aur method `area()` jo area return kare.

# step 1:
# Ek `Circle` class with `radius` aur method `area()` jo area return kare.

# step 2:   circle(3).area = 78.53975s

# step 3:
# 1: class mai Cirle word do.
# 2: def mai __init__ mai self he word common hai likhana padta hai.
# 3: self.radius = radius digiye
# 4: or fir formula do return mai pie ki value do * radius ** 2 do ye area ka formula hai.
# 5: print mai class do usme value do fir .area do.

# step 4:

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        # formula: pie = 3.14159
      return 3.14159 * self.radius ** 2
print(Circle(5).area())

# step 5:

"""
153.93791

"""