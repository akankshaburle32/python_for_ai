# que 1:
## Computer class banao jo CPU aur RAM objects rakhe (composition).

# step 1:
## Computer class banao jo CPU aur RAM objects rakhe (composition).

# step 2:

# step 3:

# 1: CPU ka class lo. usme def mai __init__ method lo. attribute lo.
# 2: RAM ka class lo. usme def mai __init__ method lo. attribute lo.
# 3: Computer ka class lo. def mai __init__ method lo. or usme CPU or Ram ka class usme add karo.
# 4: print mai dono ki value do.

# step 4:

class CPU:
    def __init__(self, brand):
        self.brand = brand

class RAM:
    def __init__(self, size):
        self.size = size

class Computer:
    def __init__(self):
        self.cpu = CPU("Intel")
        self.ram = RAM("8GB")

Computer = Computer()

print("--------------------------")
print(Computer.cpu.brand)
print(Computer.ram.size)
print("--------------------------")

# step 5:

"""
----------------
Intel
8GB
----------------

"""