# que 5:

"""
### Project 5 — Tip Calculator
- **EN:** Write a function `tip_amount(bill, percent)` that returns how much tip to pay. Then print the total bill (bill + tip) for a ₹800 bill at 10%.
- **हिंदी:** एक function `tip_amount(bill, percent)` बनाओ जो tip की रकम **return** करे। फिर ₹800 के bill पर 10% tip के साथ कुल bill (bill + tip) print करो।
- **Concepts:** `return`, using the returned value in more maths
- **Hint:** `return bill * percent / 100`, then `total = bill + tip_amount(800, 10)`.

"""

# step 1:
## Ek fun "tip_amount(bill, percent)" banao jo tip ki rakkam **return** kare. fir ₹800 ke bill par 10% tip ke saath kuli bill (bill + tip) print karo.

# step 2: ex.  bill * percent / 100  = 800, 10 >> 880.0

# step 3:

# 1: def mai fun mai 2 parameter do.
# 2: total mai 0 do.
# 3: tip mai formula do.
# 4: total mai bill add tip karo.
# 5: return mai total do quvki vo return karke value degi.
# 6: print mai fun do usme value do.

# step 4:

def tip_amount(bill, percent):
    total = 0
    tip = bill * percent / 100
    total = bill + tip
    return total
print(tip_amount(800, 10))



# step 5:

"""
880.0

"""