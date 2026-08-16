# que 35:
## names → scores ki dict di hai. Sabse zyada score wala naam print karo.
# Given: scores = {"Asha": 40, "Ravi": 85, "Zoya": 70}

# step 1:
## names → scores ki dict di hai. Sabse zyada score wala naam print karo.

# step 2:

# step 3:

# 1: sores ki dict banao.
# 2: high = 0, name = " " likho.
# 3: for mai if scores[student] > high: jo bada hoga vo print hoga.
# print mai name student = name deya to.

# step 4:

scores = {
            "Asha": 40,
            "Ravi": 85,
            "Zoya": 70
          }

high = 0
name = " "

for student in scores:
    if scores[student] > high:
        high = scores[student]
        name = student

print(name)

# step 5:

#  student  score    highest     name  
#   -         -         -         - 
#  Asha       40       40      Akash 
#  Ravi       85       85      Rahul 
#  zoya       70       85      Rahul 

# print Ravi