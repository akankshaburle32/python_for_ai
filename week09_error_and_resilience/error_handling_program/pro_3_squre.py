# que 3:

# User se ek number input lo aur uska square print karo.

# Conditions:

# Agar user number enter kare → square print karo.
# Agar user number ki jagah text enter kare → "Invalid input" print karo.
# try aur except ValueError use karo.

try:
    num = int(input("Enter the sq. no. :" ))
    print(num ** 2)

except ValueError:
    print("Invalid input")

finally:
    print("Square completed")