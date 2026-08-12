# c44:  que 3:
## `Employee` parent with `work()`; `Developer` aur `Designer` children jo alag-alag work print karein.

# step 1:
## `Employee` parent with `work()`; `Developer` aur `Designer` children jo alag-alag work print karein.

# step 2:

# step 3:

# 1: class mai parent do. def mai work method lo usme self lo. print mai kuch bhi likh sakte hai.
# 2: class mai 1st child lo usme parent lo. def mai work method lo usme self lo. print mai kuch bhi do.
# 3: class mai 2nd child lo usme mai parent lo. def mai work mwthod lo usme self lo print mai kuch likho.
# 4: dev = Developer() lo.
# 5: des = Designer() lo.
# 6: dev.work(), des.work() print ho jayga.

# step 4:

class Employee:
    def work(self):
        print("Working")

class Developer(Employee):
    def work(self):
        print("Writing code")

class Designer(Employee):
    def work(self):
        print("Designer UI")

dev = Developer()
des = Designer()

dev.work()
des.work()

# step 5:

"""
Writing code
Designer UI

"""