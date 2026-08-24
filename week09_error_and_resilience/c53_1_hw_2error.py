# c53:  que 1:
# ek program jo list se index access kare, ValueError or IndexError handle kare.

numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except ValueError:
    print("Please enter a valid number.")

except IndexError:
    print("Index is out of range.")