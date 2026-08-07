# que 12:

"""
### Project 12 — Class Average (`*args` with a guard)
- **EN:** Write `average(*marks)` that returns the average of any number of marks. If called with no marks, return 0 (avoid divide-by-zero).
- **हिंदी:** `average(*marks)` बनाओ जो कितने भी marks का average **return** करे। अगर बिना marks के call हो तो 0 return करो (divide-by-zero से बचो)।
- **Concepts:** `*args`, `len()`, guard condition
- **Hint:** `if len(marks) == 0: return 0` first, then `return sum(marks) / len(marks)`.

"""

# step 1:
## "average(*marks)" banao jo kitne bhi marks ka average **return** kare. agar bina marks ke call ho to 0 return karo (divide-by-zero se bacho).

# step 2:  len = 0 >> (avrage(0))

# step 3:

# 1: def mai fun lo or usme *argu lo.
# 2: if mai len(marks) == 0: do.
# 3: return = 0 do.
# 4: retun mai formula do.
# 5: print mai fun mai value mat do.

# step 4:

def average(*marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

print(average())    

# step 5:

"""
0

"""