# c44:  que 1:
## `Shape` parent; `Triangle` aur `Square` children, dono ka apna `area()`.

# step 1:
## `Shape` parent; `Triangle` aur `Square` children, dono ka apna `area()`.

# step 2:

# step 3:

# 1: class mai parent lo.
# 2: def mai __init__ lo or common word ek para. attribute lo.
# 3: class mai 1st child lo. usme(parent lo). def mai __init__ usme common word or para 3 lo name base height lo. automatacally sper() aajata hai or attribute lo 2 no ke. 
# 4: def mai area lo usme self lo. return mai formula lo triangle ka.
# 5: class mai 2nd child lo. usme(parent lo). def mai __init__ usme common word or para 2 lo name side lo. automatacally sper() aajata hai or attribute lo 1 no ke. 
# 6: def mai area lo usme self lo. return mai formula lo Square ka.
# 7: t = Triangle mai value do. or s = Square mai value do.
# 8: print mai Triangle mai 3 para do. or print mai Square 2 para do.

# step 4:

class Shape:
    def __init__(self, name):
        self.name = name

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)        
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)   
        self.side = side 

    def area(self):
        return self.side * self.side    

t = Triangle("Triangle", 34, 6)
s = Square("Square", 8)     

print(t.name, t.base, t.height)
print(s.name, s.side)

# step 5:

"""
Triangle 34 6
Square 8

"""