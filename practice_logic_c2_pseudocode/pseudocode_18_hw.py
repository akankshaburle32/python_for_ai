# que 18:
## Ek word diya hai. Uska reverse banao aur print karo.
# Given: word = "hello"   →  "olleh"

# step 1:
# Ek word diya hai. Uska reverse banao aur print karo.

# step 2:   ex: "hello"   →  "olleh"

# step 3:

# 1: result mai " " iska ye mtlab hota hai ki isme kuch nhi hai
# 2: for mai hum hello ki jagh hamane p likha. 
# 3: result mai p + result likhoge.
# 4: print mai result likhiye

# step 4:


result = ""
for p in "hello":
    result = p + result
print(result)


# step 5: 

# step      result      p
# f-lp1     " "         h
# f-lp1     "h"         h
# f-lp2     "h"         e
# f-lp2     "eh"        e
# f-lp3     "eh"        l
# f-lp3     "leh"       l
# f-lp4     "leh"       l
# f-lp4     "lleh"      l
# f-lp5     "lleh"      o
# f-lp5     "olleh"     o
# print("olleh")