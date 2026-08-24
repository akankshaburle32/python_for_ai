# que 1:

"""
### Project 1 — Room Area Calculator
- **EN:** Write a function `room_area(length, width)` that returns the area of a room. Use it to find the area of 3 different rooms and print each result.
- **हिंदी:** एक function `room_area(length, width)` बनाओ जो कमरे का area **return** करे। इसे 3 अलग-अलग कमरों का area निकालने के लिए इस्तेमाल करो और हर result print करो।
- **Concepts:** `def`, two parameters, `return`, function call
- **Hint:** `return length * width`. Print the call: `print(room_area(10, 12))`.

"""

# step 1:
# Ek function room_area(length, width) banao jo kamre ka area **return** kare. is 3 alag alag kamreo ka area nikalna ke istemal karo or har result print karo.

# step 2:  ex: length = 10, width = 12 >> area = 120

# step 3:

# 1: def mai ek fun lo or usme parameter do. (room_area(length, width))
# 2: return mai length * width do. quvki legth or width ka multipy karne ke liye.
# 3: input mai length do or input mai width do.
# 4: print mai (room_area(length, width)) area print karga isiye fun or parameter do.

# step 4:

def room_area(length, width):

    return length * width

length = int(input("Enter the length of the room: "))
width = int(input("Enter the width of the room: "))
print("The area of the room is: ", room_area(length, width))

# step 5:

"""
Enter the length of the room: 10
Enter the width of the room: 12
The area of the room is: 120

"""