# que 6:

# Program user se:

# Student name
# 3 subject marks

# input le aur total, percentage aur grade print kare.

# Error Handling lagao:

# Agar user marks ki jagah text enter kare → ValueError handle karo.
# Agar marks 0–100 ke bahar ho → proper error message do.
# Program error aane ke baad bhi crash nahi hona chahiye.

# 👉 Hint: try, except, else, finally use karne ki koshish karo.

try:
    name = input("Enter the name : ")

    marks1 = int(input("Enter the 1st sub marks : "))
    marks2 = int(input("Enter the 2nd sub marks : "))
    marks3 = int(input("Enter the 3rd sub marks : "))

    # marks Validation
    if not 0 <= marks1 <= 100 and 0 <= marks2 <= 100 and 0 <= marks3 <= 100:
        raise ValueError("Marks should be between 0 and 100.")

except ValueError as e:
    print("Error :", e)

else: 
    total = marks1 + marks2 + marks3
    percentage = total / 3

    if percentage >= 90:
        grade = "A"

    elif percentage >= 75:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 40:
        grade = "D"

    else:
        grade = "E"

    print("\n Student Name :", name)
    print("Total :", total)
    print("Percentage :", percentage)
    print("Grade :", grade)

finally:
    print("Program Completed")