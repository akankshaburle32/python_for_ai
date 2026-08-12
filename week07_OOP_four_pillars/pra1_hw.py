# que 1:
## person class banao our student class usses inherit kare. student mein study() method ho.

# step 1:
## person class banao our student class usses inherit kare. student mein study() method ho.

# step 2:

# step 3:

# 1: person ka ek clss banao.
# 2: def mai __init__ method lo. usme self ek para do. aatribute do.
# 3: student ka class banao. usme person lo.
# 4: def mai study method do usme self lo. print mai f string lo usme atribute lo or jo out mai dena hai vo likho.
# 5: student mai value do .method do.

# step 4:

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(f"{self.name}, Hardworking")

Student("Chaku").study()                

# step 5:

"""
Chaku, Hardworking

"""