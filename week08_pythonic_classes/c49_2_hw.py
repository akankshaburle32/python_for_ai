# c49:  que 2:
## Person class mein age property + setter banao jo negative age reject kare.

# step 1:
## Person class mein age property + setter banao jo negative age reject kare.

# step 2:

# step 3: 

# 1: person la class lo.
# 2: def mai __init__ mrthod lo.
# 3: attribute lo.
# 4: @ property lo.
# 5: def mai age method lo.
# 6: return mai attribute.
# 7: @age.setter do.
# 8: def mai age method lo.age >= 0: lo. attribute do.
# 9: if mai age >= 0: lo. attribute do.
# 10: else mai print mai "Invalid age" do.
# 11: P = Person(value)
# 12: print(p.age)
# 13: P.age - value do.


class Person:
    def __init__(self, age):
        self.age  = age

    @property
    def age(self):
        return self._age

    @age.setter    
    def age(self, age):
        if age >= 0:
            self._age = age

        else:
            print("Invalid age")

P = Person(20)
print(P.age)

P.age = -7

# step 5:

"""
20
Invalid age

"""