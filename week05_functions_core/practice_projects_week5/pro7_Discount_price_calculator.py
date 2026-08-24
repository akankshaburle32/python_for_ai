# que 7:

"""
### Project 7 — Discount Price Calculator
- **EN:** Write a function `final_price(price, discount_percent)` that returns the price after discount. Print the final price of a ₹1500 item with 20% off.
- **हिंदी:** एक function `final_price(price, discount_percent)` बनाओ जो discount के बाद की कीमत **return** करे। ₹1500 के item पर 20% छूट के बाद final price print करो।
- **Concepts:** `return`, percentage maths
- **Hint:** `return price - (price * discount_percent / 100)`.

"""

# step 1:
## Ek fun "final_price(price, discount_percent)" banao jo discount ke baad ki kimat **return** kare. ₹1500 ke item par 20% choot ke baad final price print karo.

# step 2: ex. 1500 * 20/100 = 1200.0

# step 3:

# 1: def mai fun mai 2 parameter do.
# 2: return mai 2 parameter ka multi or / 100 karo.
# 3: print mai fun or value.


# step 4:

def final_price(price, discount_percent):
    return price - (price * discount_percent / 100)

print(final_price(1500, 20))

# step 5:

"""
1200.0

"""