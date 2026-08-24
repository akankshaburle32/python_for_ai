# c52:  que 3:
# ek try/except/else/finally ka poora ex. likho jo chharo blocks dikhaye.

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    marks = int(input("Enter your marks: "))

except ValueError:
    print("Invalid input! Please enter numbers for age and marks.")

else:
    print("\nStudent Details:")
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)

    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

finally:
    print("\nProgram completed.")