# que 4:

# Ek list banao:

# numbers = [10, 20, 30, 40]

# User se index input lo aur us index ka element print karo.

# Valid index → element print ho.
# Invalid index → "Index not found" print ho.
# try + except IndexError use karo.

numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter index :"))
    print(numbers[index])

except IndexError:
    print("Index not found")

finally:
    print("index completed")    