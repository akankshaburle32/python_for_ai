# c43:  que 3:
## `Employee` parent (name, salary); `Manager` child jo `super()` use kare aur ek `team_size` add kare.

# step 1:
## `Employee` parent (name, salary); `Manager` child jo `super()` use kare aur ek `team_size` add kare.
 
# step 2:

# step 3:

# 1: class mai Employee lo.
# 2: def __init__ mai common ek word do.
# 3: or attribute do.
# 4: class mai Manger mai emloyee lo.
# 5: def mai __init__ ek common word jitna bhi employee mai hota hai usme do or ek add karo.
# 6: super() atomatically aa jati hai.
# 7: or attribute.
# 8: manager mai value do.
# 9: print mai manager ke parameter do.

# step 4:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manger(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

m = Manger("Chaku", 50000, 10)         
print(m.name, m.salary, m.team_size)

# step 5:

"""
Chaku 50000 10

"""