# que 6:

"""
### Project 6 — Even or Odd Checker
- **EN:** Write a function `is_even(n)` that **returns** `True` if the number is even, else `False`. Use it in a loop to print which numbers in `[3, 8, 15, 22, 41]` are even.
- **हिंदी:** एक function `is_even(n)` बनाओ जो number even होने पर `True`, वरना `False` **return** करे। इसे loop में इस्तेमाल करके बताओ `[3, 8, 15, 22, 41]` में कौन-से numbers even हैं।
- **Concepts:** returning a boolean, `%`, using a function in a loop
- **Hint:** `return n % 2 == 0`.

"""

# step 1:
## Ek fun "is_even(n)" banao jo no. even hone par "True", varna "False" **return** kare. is loop mai istamal karke banao "[3, 8, 15, 22, 41]" mai kon- se no. even hai.

# step 2:  2 = True, 5 = False

# step 3:

# 1: def mai fun mai parameter do.
# 2: return mai n % 2 == 0 do.
# 3: for mai p mai list do.
# 4: print mai p, fun or usme p do.

# step 4:

def is_even(n):
        return n % 2 == 0

for p in [3, 8, 15, 22, 41]:

    print(p, is_even(p))    


# step 5:

"""
3 = False
8 = True
15 = False
22 = True
41 = False

"""