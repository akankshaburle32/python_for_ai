# que 17:

"""
### Project 17 — Calculator Refactor (many small functions)
- **EN:** Refactor a calculator into functions: `add`, `subtract`, `multiply`, `divide` (handle divide-by-zero by returning a message). Then write `calculate(a, b, op)` that calls the right one based on `op` (`"+"`, `"-"`, `"*"`, `"/"`).
- **हिंदी:** Calculator को functions में बाँटो: `add`, `subtract`, `multiply`, `divide` (divide-by-zero पर message return करो)। फिर `calculate(a, b, op)` बनाओ जो `op` (`"+"`, `"-"`, `"*"`, `"/"`) के हिसाब से सही function call करे।
- **Concepts:** many functions, dispatch with `if/elif` or `match`, `return`
- **Hint:** In `divide`, `if b == 0: return "Cannot divide by zero"`.

"""

# step 1:
## calculator ko functions mai baato "add", "subract", "multiply", "divide" (divide-by-zero par message return karo). fir "calculate(a, b, op)" banao jo "op" ("+", "-", "*", "/") ke hisab se sahi function call kare.

# step 2: 1+2=3, 1-2=-1, 1*2=2, 2/2=1.0

# step 3:

# 1: def mai fun or usme parameter do ise 4 time karna hai sirf oprator badlna hai (+, -, *, /) e dalne hai usme.
# 2: print mai ("============= welcome to calculate refactor =============")
# 3: while loop mai code karo.
# 4: 4 oprator hai to if, elif, elif, elif or else dena hai. 
# 5: break dena.


# step 1:

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2 

print("=============== welcome to calculator Refactor =======================") 

while True:
    num1 = int(input("Enter the 1st no. : "))
    num2 = int(input("Enter the 2nd no. : "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == "+":
        print("Addition of 2 no. is :", add(num1, num2))

    elif operator == "-":
        print("Subtraction of no. is :", sub(num1, num2))

    elif operator == "*":
        print("Multiplication of no. is :", multi(num1, num2))

    elif operator == "/":
        print("Division of 2 no. :", div(num1, num2))

    else:
        print("invalid operator")

    want_to_continue = input("Do you want continue? (y/n): ")
    if want_to_continue == "n":
        break

# step 5:

""" 
======================= welcome to calculate Refactor =========================
Enter the 1st no. : 9 
Enter the 2nd no. : 7
Enter the operator (+, -, *, /): 16
# Do you want continue? (y/n):

"""