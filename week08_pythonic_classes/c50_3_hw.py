# c50:  que 3:
## Computer class banao jo CPU aur RAM objects hold kare (composition).

# step 1:
## Computer class banao jo CPU aur RAM objects hold kare (composition).

# step 2:

# step 3:

# 1: CPU ka class banao usme def mai __init__ mai common word jeseki self. or usme attribute lo. usme "Intel".
# 2: RMA ka class banao usme def mai __init__ mai common word jeseki self. or usme attribute lo. usme "8GB".
# 3: Computer ka class banao usme def mai __init__ mai common word jeseki self. or usme attribute lo. usme CPU or RAM.
# 4: computer vala object lo.
# 5: print mai value do 2 baar CPU, RAM ka. 

# step 4:

class CPU:
    def __init__(self):
        self.name = "Intel"

class RAM:
    def __init__(self):
        self.name = "8GB"

class Computer:
    def __init__(self):        
        self.cpu = CPU()                                                                                            
        self.ram = RAM()

computer = Computer()

print(computer.cpu.name)
print(computer.ram.name)

# step :

"""
Intel
8GB

"""