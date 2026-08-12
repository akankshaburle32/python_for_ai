# c45:  que 3:
## Ek abstract `PaymentMethod` with abstract `pay(amount)`; `Cash` aur `Card` se implement karo.

# step 1:
## Ek abstract `PaymentMethod` with abstract `pay(amount)`; `Cash` aur `Card` se implement karo.

# step 2:

# step 3:

# 1: PaymentMethod naam ki ek abstract class banao;
# 2: pay naam ki method lo. usme self or amount do.
# 3: Cash naam ki class banao. def mai pay method mai self, amount lo.
# 4: Card naam ka class banao. def mai pay naam ki method lousme self, amount lo.
# 5: cash = Cash(), card  = Card()
# 6: cash.pay(value do), card.pay(value do).

# step 4:

from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class Cash(PaymentMethod):
    def pay(self, amount):
        print("Cash Payment : ", amount)

class Card(PaymentMethod):
    def pay(self, amount):
        print("Card Payment : ", amount)

cash = Cash()
card = Card()

cash.pay(600)
card.pay(1000)

# step 5:

"""
Cash Payment : 600
Card Payment : 1000

"""