# c52:  que 2:
# safe int conversion : user input ko int banao, ValuError handle karke "Invalid" bolo.

try:
    num = int(input("Enter the no. : "))
    print("Number :", num)

except ValueError:
    print("Invalid")    

finally:
    print("Program Completed")    