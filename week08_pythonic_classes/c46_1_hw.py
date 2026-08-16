# c46:  que 1:
## Student class mein _str_ add karo jo "NAME scored MARKS" return kare.

# step 1:
## Student class mein _str_ add karo jo "NAME scored MARKS" return kare.

# step 2:

# step 3:

# 1: Student ka class banao.
# 2: def mai __init__ method lo.
# 3: attribute lo.
# 4: def mai __str__ method lo.
# 5: return mai f string lo usme attribute do.
# 6: Student mai value do.
# 7:print S.

# step 4:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
         
    def __str__(self):
        return f"NAME : {self.name}, Scored MARKS : {self.marks}"

S = Student("Chakuli", 96)        
print(S)

# step 5:

"""
NAME : Chakuli, Scored MARKS : 96

"""