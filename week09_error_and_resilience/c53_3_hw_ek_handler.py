# c53:  que 3:
# Do errors (ZeroDivisionError, ValueError) ko ek hi handler se pakdo.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except (ZeroDivisionError, ValueError):
    print("Invalid input or division by zero.")