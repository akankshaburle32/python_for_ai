# c41:      que 2:
## Ek `Student` class with `name`, `marks`, aur method `report()` jo report print kare. 2 objects banao.

# step 1:
# Ek `Student` class with `name`, `marks`, aur method `report()` jo report print kare. 2 objects banao.

# step 2: 

# step 3: 
# 1: class mai student digiye.
# 2: def mai __inti__ mai self or 2 parameter.
# 3: def mai report or usme report do.
# 4: print mai f string {self.name} scored {self.marks} ye do. 
# 5: student mai name do or marks. report mai ise 2 baar kijiye.

# step 4:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def report(self):
        print(f"{self.name} scored {self.marks}")
Student("CHAKU", 85).report()
Student("BHUMI", 90).report()

# step 5:

""" 
CHAKU scored 85
BHUMI scored 90

"""