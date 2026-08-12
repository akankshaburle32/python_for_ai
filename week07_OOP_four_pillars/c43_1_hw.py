# c43:  que 1:
## `Animal` parent banao; `Cat` aur `Cow` children banao, har ek apni awaaz wala method.

# step 1:
## `Animal` parent banao; `Cat` aur `Cow` children banao, har ek apni awaaz wala method.

# step 2:

# step 3:

# 1: claas mai parant banao.
# 2: def mai __init__ mai ek common word do or ek parameter.
# 3: or attribute do.
# 4: class mai 1st child do or method do. or print mai f string mai method do.
# 5: class mai 2nd child do or usme method do. print mai f string mai method do.
# 6: 1st value do. method do(). ise 2 baar karo. 

# step 4:

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def sound(self):
        print(f"{self.name} says meow")

class Cow(Animal):
    def sound(self):
        print(f"{self.name} says moo")

Cat("mausi").sound()
Cow("gaumata").sound()                


# step 5:

"""
mausi says meow
gaumata says moo

"""
