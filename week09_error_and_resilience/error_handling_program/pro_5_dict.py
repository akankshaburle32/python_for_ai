# que 5:

# Dictionary:

# student = {
#     "name": "Akanksha",
#     "age": 18,
#     "city": "Nagpur"
# }

# User se key input lo aur uski value print karo.

# Key available → value print ho.
# Key available nahi → "Key not found" print ho.
# try + except KeyError use karo.

student = {
                "name": "Akanksha",
                "age": 18,
                "city": "Nagpur"
           }

try: 
    key = input("Enter key : ")
    print(student[key]) 

except KeyError:
    print("key not found")

finally:
    print("key completed")                  