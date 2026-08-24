# c54:  que 3:
## Ek `BankAccount` class (Week 7) mein `withdraw` ko custom `InsufficientFundsError` raise karwao.

# step 1:
## Ek `BankAccount` class (Week 7) mein `withdraw` ko custom `InsufficientFundsError` raise karwao.

# step 2:

# step 3:

# 1: InsufficientFoundError class banao usme Exception do.
# 2: BankAccount ka class banao. usme def mai fun lo.  or usme para do usme attribute lo.
# 3: def mai withdraw ka fun lo usme para lo. if mai 2nd fun > 1st attribute do. raise mai konsa error hai to.
# 4: attribute -= 2nd para return mai attribute do.
# 5: ek var banao usme 2nd class or usme value do.
# 6: try mai print mai var.2nd fun usme value do.
# 7: except mai kis condition mai error hai batao.

# step 4:

class InsufficientFoundError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFoundError("Insufficient founds")

        self.balance -= amount
        return self.balance   

account = BankAccount(5000)

try:
    print(account.withdraw(6000))

except InsufficientFoundError as e:
    print(f"Error : {e}")  

# step 5:

"""
Error : Insufficient founds

"""