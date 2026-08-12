# c41:  que 1:
## Ek `Car` class banao with `brand`, `speed`, aur ek method `drive()` jo "BRAND is driving at SPEED" print kare.

# step 1: 
# Ek `Car` class banao with `brand`, `speed`, aur ek method `drive()` jo "BRAND is driving at SPEED" print kare.

# step 2: 

# step 3: 

# 1: class mai Car do.
# 2: def mai __inti__ or usme self common hai or do parameter do.
# 3: def mai drive do usme slf do vo common hai isiye.
# 4: print mai f string do {self.brand}  is driving at {self.speed} km/h do.
# 5: Car mai ek naam do or ek speed do .drive do.

# step  4:

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h")
Car("Chakuli", 80).drive()

# step 5: 

"""
Chakuli is driving at 80 km/h

"""