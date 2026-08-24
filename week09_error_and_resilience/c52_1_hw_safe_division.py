# c52:  que 1:
## Safe division : do no. lo, divide karo ZeroDivisionError handle karo.

# step 1:
## Safe division : do no. lo, divide karo ZeroDivisionError handle karo.

# step 2:

# step 3:

# 1: try : user se 2 no. do .
# 2: print mai divide karo.
# 3: except mai error do.
# 4: finally mai kuch bhi likho.

# step 4:

try:
    a = int(input("Enter the 1st no. : "))
    b = int(input("Enter the 2nd no. : "))
    print("Result: ", a / b)

except ZeroDivisionError:
    print("cannot divide by Zero.")

finally:
    print("Division Completed")    

# step 5:

"""
Enter the 1st no. : 4
Enter the 2nd no. : 4
Result: 1.0
Division Completed
"""