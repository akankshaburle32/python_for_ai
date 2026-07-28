# c20    que 2:
## Menu calculator ko run karke saare 4 operations test karo.

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int (input ("Enter first choice (1-4): "))

a = int (input ("Enter first no. : "))
b = int (input ("Enter second no. : "))

if choice == 1:
    print("Result = ", a + b)

elif choice == 2:
    print("Result =", a - b)

elif choice == 3:
    print("Result =", a * b)

elif choice == 4:
    if b != 0:
      print("Result =", a / b )

    else:
      print("Division by zero is not allowed. ")
else: 
    print("Invalid choice")                      