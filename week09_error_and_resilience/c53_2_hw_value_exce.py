# c53:  que 2:
# int(input) mein ek try with ValueError or ek general Exeption fallback.

try:
    num = int(input("Enter number: "))
    print("Number:", num)

except ValueError:
    print("Please enter a valid integer.")

except Exception:
    print("Something went wrong.")