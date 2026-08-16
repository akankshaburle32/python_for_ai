# c47:  que 1:
## Money class (amount) mein _eq_ add karo taaki same amount wale objects equal ho.

# step 1:
## Money class (amount) mein _eq_ add karo taaki same amount wale objects equal ho.

# step 2:

# step 3:

# 1: Money ka class lo.
# 2: def mai __init__ method lo. or attribute do.
# 3: def mai __eq__ method lo. return mai attribute lo == aatritube lo.
# 4: print mai value do.

# step 4:

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, cash):
        return self.amount == cash.amount

print(Money(500) == Money(500))


# step 5:

"""
True

"""
















