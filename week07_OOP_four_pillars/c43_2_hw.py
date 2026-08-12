# c43:  que 2:
## `Shape` parent (with `name`); `Square` aur `Rectangle` children with `super()`.

# step 1: 
## `Shape` parent (with `name`); `Square` aur `Rectangle` children with `super()`.
# step 2:

# step 3:

# 1: class mai Shape lo.
# 2: def mai __init__ lo or usme common word lo or para. or niche aatribute lo.
# 3: class mai squre lo usme Shape lo.
# 4: def mai __init__ mai common word or parameter lo Squre mai side hoti hai na ho side lo. super() attomatically hota hai. parent jaisa. or attribute do.
# 5: calss mai REctangle lo usme Shape lo.
# 6: def mai __init__ mai common word or parameter lo Rectangle mai length, width hoti hai na ho length, width lo. super() attomatically hota hai. parent jaisa. or attribute do.
# 7: s = Square(value do isme) r = (value do isme).
# 8: print mai square or rectangle ke value do ek ek karke.

# step 4:

class Shape:
    def __init__(self, name):
        self.name = name

class Squre(Shape):
    def __init__(self, name, side):
        super().__init__(name) 
        self.side = side

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)               
        self.length = length
        self.width = width

s = Squre("Square", 7)
r = Rectangle("Rectangle", 24, 6)        

print(s.name, s.side)
print(r.name, r.length, r.width)

# step 5:

"""
Square 7
Rectangle 24 6

"""