# c32:   que 2:
## intro(name, age, city="India") banao; ek baar city ke saath, ek baar bina, call karo.

# step 4:

def intro(name, age, city="India"):
    return f"{name}, {age}, form {city}"
print(intro("Chakuli", 16))
print(intro("Chakuli", 16, "Sindi")) 
   