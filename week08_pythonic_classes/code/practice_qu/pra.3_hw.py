# que 3:
## 3. @property — Student

# Student class banao:

# name aur _marks attributes rakho.
# @property se marks ko access karo.
# marks change karte waqt value 0 se 100 ke beech honi chahiye.
# @marks.setter use karo.

# step 1:

# step 2:

# step 3:

# 1: name aur _marks attributes rakho.
# 2: @property se marks ko access karo.
# 3: marks change karte waqt value 0 se 100 ke beech honi chahiye.
# 4: @marks.setter use karo.

# step 4:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value > 100:
            raise ValueError("Marks cannot be aagrater than 100.")

        self._marks = value

S = Student("Chaku", 85)

print(S.marks)


# step 5:

"""
85

"""