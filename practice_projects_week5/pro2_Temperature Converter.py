"""
### Project 2 — Temperature Converter
- **EN:** Write a function `celsius_to_f(c)` that converts Celsius to Fahrenheit and **returns** the value. Test it with 0, 37, and 100 degrees.
- **हिंदी:** एक function `celsius_to_f(c)` बनाओ जो Celsius को Fahrenheit में बदल कर value **return** करे। इसे 0, 37 और 100 डिग्री पर test करो।
- **Concepts:** `def`, arithmetic, `return`
- **Hint:** Formula: `(c * 9 / 5) + 32`.

"""

# step 1:
## Ek fun lo "celsius_to_f(c)" banao jo celsius ko fahrenheit me badal kar value **return**  kare. is 0, 37 or 100 degree par test karo.

# step 2: ex:  (c *(9/5) + 32)  ise formulo solve karke jo ans aayga vo. print(celsius_to_f(100))  = 188.6

# step 3:

# 1: def mai ek fun do or usme parameter do.
# 2: retun mai formula de sakte hai.
# 3: print mai function or usme parameter do ise 3 baar karna hai alag alag value do.

# step 4:

def celsius_to_f(c):
    return (c *(9/5) + 32)

print(celsius_to_f(0))
print(celsius_to_f(37))
print(celsius_to_f(100))

# step 5:

"""

32.0
98.6000
212.0

"""