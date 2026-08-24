# que 19:

"""
### Project 19 — Restaurant Bill (combine everything)
- **EN:** Write `restaurant_bill(*prices, tax=5, tip=0)` that returns the final total: sum of all item prices, plus `tax`%, plus `tip`%. Call it with `tax` defaulted and `tip=10` passed as a keyword argument.
- **हिंदी:** `restaurant_bill(*prices, tax=5, tip=0)` बनाओ जो final total **return** करे: सभी item prices का जोड़, फिर `tax`%, फिर `tip`%। इसे एक बार `tax` को default रखते हुए और `tip=10` keyword argument देकर call करो।
- **Concepts:** `*args` + keyword-only-style defaults together, percentage maths
- **Hint:** `subtotal = sum(prices)`, then add `subtotal * tax / 100` and `subtotal * tip / 100`.

"""

# step 1:
## "restaurant_bill(*prices, tax=5, tip=0)" banao jo final total **return** kare: sabhi item prices ka jod, fir "tax %" fir "tip"%। is ek baar "tax" ko defalt rakhte hue or "tip=10" keyword argument dekar call karo.

# step 2:

# step 3:

# 1: def mai fun *argu parameter do.
# 2: var mai sum argu do.
# 3: total mai var * parameter / 100 + var * parameter / 100 lo.
# 4: return mai total.
# 5: print mai fun mai value do. ise 2 baar kare.

# step 4:

def restaurant_bill(*prices, tax=5, tip=0):
    subtotal = sum(prices)
    total = subtotal * tax / 100 + subtotal * tip / 100
    return total

print(restaurant_bill(30, 67, 29))
print(restaurant_bill(30, 67, 29, tip=10))

# step 5:

"""
6.3
18.9

"""