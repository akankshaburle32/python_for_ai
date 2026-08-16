# c47:  que 2:
## Cart class mein _len_ add karo jo items list ki size de.

# step 1:
## Cart class mein _len_ add karo jo items list ki size de.

# step 2:

# step 3:

# 1: Cart ka class banao. def mai __init__ method lo. self.item = [] items store karna hai.
# 2: def mai add method lo. self.item.append karo. hame item add karna hai to.
# 3: def __len__ lo hame len nikalni hai item ki.
# 4: C = Cart mai value do.
# 5: print(len(C)) do.

# step 4:

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
   
    def __len__(self):
        return len(self.items)

C = Cart(); C.add("Chaku"); C.add("Bhumi")
print(len(C))

# step 5:

"""
2

"""
