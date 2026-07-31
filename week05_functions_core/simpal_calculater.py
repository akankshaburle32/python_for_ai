# que 1:
## Simpal calculater for +, -, *, /.


# step 1: Simpal calculater for +, -, *, /.

# step 2:   ex: 1+2=3, 1-2=1, 1*2=2, 2/1=0.5.

# step 3: 

# 1: konse bhi 2 no. do.
# 2: kosa bhi ek oprator do jeseki+, -, *, /.
# 3: or jo 2 no. diya hai or ek oprator diya hai uska ans nikalo kya hai karke.
# or print mai use dikhavo kya hai karke.

# step 4:

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print("==================== Welcome to Simpal Calculater =======================")

while True:
    num1 = int(input("Enter your 1st no. : "))
    num2 = int(input("Enter your 2nd no. : "))
    oprator = input("Enter your oprator (+, -, *, /) : ")

    if oprator == "+":
        print("Addition of 2 no. :", add(num1, num2))

    elif oprator == "-":
        print("Subtraction of 2 no. :", sub(num1, num2))

    elif oprator == "*":
        print("Multiplication of 2 no. :", multi(num1, num2))

    elif oprator == "/":
        print("Division of 2 no. :", div(num1, num2))

    else:
        print("Invalid oprateor")     

    want_to_continue = input("Do you want to continue (y/n) : ")
    if want_to_continue == "n":
        break

# step 5:

# print("================== Welcome to Simpal Calculater =================")
# Enter your 1st no. : 16
# Enter your 2nd no. : 4
# Enter your oprator(+, -, *, /) : +
# Addition 2 is no. : 20
              
