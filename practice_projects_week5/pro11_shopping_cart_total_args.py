# que 11:

"""
### Project 11 — Shopping Cart Total (`*args`)
- **EN:** Write `cart_total(*prices)` that returns the sum of any number of item prices. Test it with 3 prices and with 6 prices.
- **हिंदी:** `cart_total(*prices)` बनाओ जो कितने भी item prices का जोड़ **return** करे। इसे 3 prices और 6 prices के साथ test करो।
- **Concepts:** `*args`, `sum()`
- **Hint:** `return sum(prices)`. Inside, `prices` is a tuple.

"""
# step 1:
## "cart_total(*prices)" banao jo kitne bhi item prices ka jod **return** kare. ise 3 prices or prices ke saath test karo.

# step 2:  3 + 9 = 12

# step 3:

# step 1: def mai fun mai *argu do.
# step 2: return mai sum or usme fun do.
# step 3: print mai fun mai vlue do.

# step 4:

def cart_total(*prices):
    return sum(prices)
     
print(cart_total(3, 6))    


# step 5:

"""
9

"""