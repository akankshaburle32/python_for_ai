# que 10:

"""
### Project 10 — Power Function (default exponent)
- **EN:** Write `power(base, exp=2)` that returns `base ** exp`. By default it squares; but `power(2, 3)` should give 8.
- **हिंदी:** `power(base, exp=2)` बनाओ जो `base ** exp` **return** करे। Default में यह square करे; पर `power(2, 3)` का जवाब 8 आए।
- **Concepts:** default value, `**` operator
- **Hint:** `return base ** exp`. `power(5)` → 25.

"""

# step 1:
## "power(base, exp=2)" banao jo "base ** exp" **return** kare. Defalt mai yah squares; "power(2, 3)" ka javab 8 aaye.

# step 2: 3**2 = 9

# step 3:

# 1: def mai fun lo or usme parameter or defalt parameter do.
# 2: return mai 2 parameter ke bich mai double ** ise do.
# 3: print mai fun or usme value do 2 baar karo print.

# step 4:

def power(base, exp=2):
    return base ** exp

print(power(5))    
print(power(2, 3))

# step 5:

"""
25
8

"""