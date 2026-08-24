# que 21:

"""
### Project 21 — ATM Machine Simulator
- **EN:** Build an ATM with functions `check_balance(balance)`, `deposit(balance, amount)`, and `withdraw(balance, amount)` (block overdraft with a message). Run a `while` menu: 1) Balance 2) Deposit 3) Withdraw 4) Exit. Keep updating the balance from the returned values.
- **हिंदी:** एक ATM बनाओ जिसमें functions हों `check_balance(balance)`, `deposit(balance, amount)`, और `withdraw(balance, amount)` (पैसे कम हों तो message देकर रोको)। एक `while` menu चलाओ: 1) Balance 2) Deposit 3) Withdraw 4) Exit. हर बार return की गई value से balance update करते रहो।
- **Concepts:** multiple functions, `return`, `while` menu, `if/elif/else`
- **Hint:** In `withdraw`, `if amount > balance: return balance` (unchanged) with a warning; else `return balance - amount`.

"""

# step 1:

# step 2:

# step 3:

# step 4:

def check_balance(balance):
    return balance

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("fonds")
        return balance - amount



# step 5: