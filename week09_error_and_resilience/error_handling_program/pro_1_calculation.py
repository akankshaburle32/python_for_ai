# que 1: 

# User se 2 numbers input lo.
# User se operation lo: +, -, *, /
# try use karo.
# except se:
# गलत number handle karo (ValueError)
# 0 se division handle karo (ZeroDivisionError)
# else use karo — calculation successful ho to result print karo.
# finally use karo — "Calculator closed" print karo.
# Kisi invalid operation par raise ValueError use karo.

try:
    a = int(input("Enter Your 1st no. : "))
    b = int(input("Enter Your 2nd no. : "))
    Operation = input("Enter Operation (+, -, *, /) : ")

    if Operation == "+":
        result = a + b

    elif Operation == "-":
        result = a - b

    elif Operation == "*":
        result = a * b

    elif Operation == "/":
        result = a / b    

    else:
        raise ValueError("Invalid Operation")                 

except ValueError as e:
    print("error :", e)

except ZeroDivisionError:
    print("cannot divide by zero")

else:
    print("result :", result) 

finally:  
    print("calculater closed")                    
