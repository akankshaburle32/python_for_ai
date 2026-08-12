# c45:  que 2:
## Jaan-boojh kar ek child banao jo `sound()` na likhe — error padho.

# step 1:
## Jaan-boojh kar ek child banao jo `sound()` na likhe — error padho.

# step 2:

# step 3:

# 1: animal naam ka abstract ckass banao.
# 2: def mai sound naam ki method lo.
# 3: Dog naam ka class banao.
# 4: dog = Dog() ab error aayga.

# step 4:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    pass

dog = Dog()

# step 5:

""" 
error
dog = Dog()

"""