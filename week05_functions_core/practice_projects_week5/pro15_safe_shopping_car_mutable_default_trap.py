# que 15:

"""
### Project 15 — Safe Shopping Cart (mutable-default trap)
- **EN:** Write `add_item(item, cart=None)` correctly so that each fresh call (without a cart) starts with an EMPTY cart. Call it 3 separate times and show each returns only its own item. (Do NOT use `cart=[]` — explain in a comment why.)
- **हिंदी:** `add_item(item, cart=None)` सही तरीके से बनाओ ताकि हर नई call (बिना cart के) खाली cart से शुरू हो। इसे 3 अलग बार call करके दिखाओ कि हर बार सिर्फ़ अपना item आता है। (`cart=[]` मत इस्तेमाल करो — comment में कारण लिखो।)
- **Concepts:** mutable default trap, `None` sentinel, `is None`
- **Hint:** `if cart is None: cart = []` — this makes a fresh list every call.

"""

# step 1:
## "add_item(item, cart=None)`" sahi tarike se banao taki har nai call (bina cart ke) khali cart se shuru ho. ise 3 alag baar call karke dikhao ki har baar sirf apna item aata hai. (cart=[] mat istemal karo - comment mai karan likho)

# step 2:                                                       

# step 3:

# 1: def mai ek fun do or usme parameter.
# 2: if mai cart is none hai.
# 3: cart = []
# 4: cart.append do qvki hame add karna hai to.
# 5: return mai cart do.
# 6: print mai 3 baar call karo fun mai value do.

# step 4:

def add_item(item, cart=None):
    if cart is None:
        cart = []
        cart.append(item)
    return cart

print((add_item("Tree")))
print((add_item("Mango")))
print((add_item(600)))

# step 5:

"""
['Tree']
['Mango']
[600]

"""