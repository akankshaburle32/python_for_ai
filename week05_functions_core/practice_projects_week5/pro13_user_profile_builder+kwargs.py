# que 13:

"""
### Project 13 — User Profile Builder (`**kwargs`)
- **EN:** Write `show_profile(**details)` that prints each detail as `key: value`. Call it with `name`, `age`, and `city`.
- **हिंदी:** `show_profile(**details)` बनाओ जो हर detail को `key: value` की तरह print करे। इसे `name`, `age`, और `city` के साथ call करो।
- **Concepts:** `**kwargs`, dict `.items()`, loop
- **Hint:** `for key, value in details.items(): print(f"{key}: {value}")`.

"""
# step 1:
## "show_profile(**details)" banao jo har detail ko "key: value" ki tarah print kare. ise "name", "age", or city ke saath call karo.

# step 2:  Std : 7th

# step 3:

# 1: def mai fun mai **argu do.
# 2: for mai key, value in details.items()do.
# 3: print mai f string mai key or value curli bracet mai do.
# 4: print mai fun mai value do name or age or city ki.

# step 4:

def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
print(show_profile(name="Chakuli", age=16, city="Sindi"))

# step 5:

"""
Name : Chakuli
age : 16
city : Sindi

"""
