# que 3:

"""
### Project 3 — Simple Interest Calculator
- **EN:** Write a function `simple_interest(principal, rate, years)` that returns the simple interest `(P × R × T) / 100`. Print interest for ₹10000 at 5% for 3 years.
- **हिंदी:** एक function `simple_interest(principal, rate, years)` बनाओ जो simple interest `(P × R × T) / 100` **return** करे। ₹10000 पर 5% की दर से 3 साल का interest print करो।
- **Concepts:** three parameters, `return`
- **Hint:** `return (principal * rate * years) / 100`.

"""

# step 1:
# Ek fun "simple_interest(principal, rate, years)" banao jo simpal interest (P × R × T) / 100 **return** kare. ₹10000 par 5% ki dar se 3 saal ka interest print karo.

# step 2:  ex.  3*4*5* = 60

# step 3:

# 1: def mai ek fun do or usme parameter do.
# 2: retun mai formula de sakte hai.
# 3: print mai function or usme parameter 3 do.

# step 4:

def simple_interest(principal, rate, years):
    return (principal * rate * years) / 100

print(simple_interest(10000, 5, 3))

# step 5:

"""
1500.0

"""