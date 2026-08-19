# que 5:
## 5. Composition + @property — Computer

# Computer class banao jo CPU aur RAM objects rakhe.

# CPU mein cores ho.
# RAM mein size ho.
# Computer ke andar CPU aur RAM objects banao.
# @property se ram_size access karo.
# Setter mein check karo ki RAM 4 GB ya usse zyada ho.
# Invalid value par "Invalid RAM size" print karo.

# step 1:
## Composition + @property — Computer

# step 2:

# step 3:

# 1: CPU mein cores ho.
# 2: RAM mein size ho.
# 3: Computer ke andar CPU aur RAM objects banao.
# 4: @property se ram_size access karo.
# 5: Setter mein check karo ki RAM 4 GB ya usse zyada ho.
# 6: Invalid value par "Invalid RAM size" print karo.

# step 4:

class CPU:
    def __init__(self, cores):
        self.cores = cores

class RAM:
    def __init__(self, size):
        self.size = size

class Computer:
    def __init__(self, cores, ram_size):
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)

    @property
    def ram_size(self):
        return self.ram.size

    @ram_size.setter
    def ram_size(self, value):
        if value > 4:
            print("Invalid RAM size")

        else:
            self.ram.size = value            

Computer = Computer(5, 6)

print()

# step 5: