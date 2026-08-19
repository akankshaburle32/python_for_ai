# que 4:
## 4. @property — BankAccount

# BankAccount class banao:

# owner aur _balance attributes rakho.
# @property se balance access karo.
# @balance.setter se balance update karo.
# Balance negative nahi hona chahiye.
# Negative value par "Invalid balance" print karo.

# step 1:
## @property — BankAccount

# step 2:

# step 3:

# BankAccount class banao:

# owner aur _balance attributes rakho.
# @property se balance access karo.
# @balance.setter se balance update karo.
# Balance negative nahi hona chahiye.
# Negative value par "Invalid balance" print karo.

# step 4:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance
        
    @balance.setter    
    def balance(self, value):
        if value < 0:
            raise ValueError("Invalid")

        self._balance = value

B = BankAccount(8, 98)        
print(B.balance)

# step 5:

"""
98

"""