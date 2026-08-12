# c44.  uqe 1:
## Ek abstract `Animal` banao with abstract `sound()`. `Dog` aur `Cat` se implement karo.

# shep 1:
## Ek abstract `Animal` banao with abstract `sound()`. `Dog` aur `Cat` se implement karo.

# step 2:

# step 3:

# 1: Animal naam ki ek abstracr class banaye.
# 2: def mai sound method lo. usme self lo.
# 3: dog ka class lo.or usme Animal do. def mai sound method lo. usme self lo.
# 4: cat ka class lo. or usme Animal do. def mai sound method lo. usme self lo.
# 5: dog = Dog(), dog.sound lo.
# 6: cat = Cat(), cat.sound lo.

# step 4:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Says : Woof")

class Cat(Animal):
    def sound(self):
        print("Cat Says : moew")

dog = Dog()
dog.sound

cat = Cat()
cat.sound

# step 5: