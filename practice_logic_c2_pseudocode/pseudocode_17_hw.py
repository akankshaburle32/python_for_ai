# que 17:
## Marks ki list di hai. Average print karo.
# Given: marks = [40, 55, 70, 90]

# step 1:
# Marks ki list di hai. Average print karo.


## step 2: ex.: 10+10+10 = 30 len =3  average = 30/3 =10

# step 3:

# 1. no. ki list lo.
# 2. total = 0
# 3. list ke pure no. ko (m) bathaye 
# 4. total = total + m
# 5. avrage = total / list me pure no. kitne hai bathaye
# 6. or uska avrage nikale

## step 4: 

marks = [40, 55, 70, 90]

total = 0
for m in marks:
    
    total = total + m
average = total / len(marks)

print(average)

 # Step 5:

 # step     marks       total       len
 # s 1      40            -          1
 # f-lp1    40            0          1
 # f-lp1    40            40         1
 # f-lp2    55            40         2
 # f-lp2    55            95         2
 # f-lp2    70            95         3
 # f-lp3    70            165        3
 # f-lp3    90            165        4
 # f-lp4    90            255        4
 # average  90            255        4
 # print(63.75)