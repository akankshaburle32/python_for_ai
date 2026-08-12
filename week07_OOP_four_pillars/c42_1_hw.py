# c41:      que 1:
## `BankAccount` mein validation add karo taaki balance kabhi negative na ho.

# step 1: 
# `BankAccount` mein validation add karo taaki balance kabhi negative na ho.

# step 2:  

# step 3:

# 1: class mai BankAccount do.
# 2: def mai __init__ mai hum self he common hai or ek parameter do.
# 3: if mai balanace < 0
# 4: print mai hum ("balance cannot be - ")
# 5: self.balance = 0 
# 6: else mai self.balance = balance
# 7: account hum object le sakte hai usme class or usme value.
# 8: ek positive value do or ek negative value do. 

# step 4:

class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            print("balance cannot be negative")
            self.balance = 0
        else:
            self.balance = balance

account = BankAccount(1000)           
print(account.balance)

account = BankAccount(-500)
print(account.balance)

# step 5:

"""
1000
balance cannot be negative
0

"""