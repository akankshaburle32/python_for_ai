# que 4:

"""
### Project 4 — Greeting Card Maker
- **EN:** Write a function `make_greeting(name, occasion)` that **returns** a message like `"Happy Diwali, Asha!"`. Do NOT print inside the function — return the string and print it outside.
- **हिंदी:** एक function `make_greeting(name, occasion)` बनाओ जो `"Happy Diwali, Asha!"` जैसा message **return** करे। Function के अंदर print मत करो — string return करो और बाहर print करो।
- **Concepts:** f-string, `return` vs `print`
- **Hint:** `return f"Happy {occasion}, {name}!"`.

"""

# step 1:
## Ek fun "make_greeting(name, occasion)" banao "Happy Diwali, Asha!" jaisa MSG **return** kare. fun ke andar print mat karo - string return karo or bahar print karo.

# step 2:  ex.  f"Good {type}" = Good Morning 

# step 3:

# 1: def mai fun mai 2 parameter do.
# 2: return mai f string mai Happy curli bracket mai alag alag parameter do.
# 3: print mai fun or usme value do. 

# step 4:

def make_greeting(name, occasion):
    return f"Happy {occasion}, {name}!"

print(make_greeting("Chakuli", "Diwali"))    


# step 5:

"""
Happy Diwali, Chakuli!

"""