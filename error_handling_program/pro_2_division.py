# que 2"

# User se 2 numbers input lo aur unka division karo.

# Program mein:

# Agar user 0 se divide kare → "Cannot divide by zero" print ho.
# Agar user number ki jagah text enter kare → "Please enter numbers only" print ho.
# Baaki cases mein division ka result print ho.

# 👉 try, except ZeroDivisionError, except ValueError use karo.

try:
    a = int(input("Enter your 1st no. :" ))
    b = int(input("Enter Your 2nd no. :"))
    print(a / b)

except  ZeroDivisionError:
       print("cannot divide by zero")

except ValueError:
        print("please enter numbers only")

finally:
    print("division completed")        