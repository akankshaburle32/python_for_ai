## Step 1 : REstateEk 
##  que 2. Ek list of marks lo aur unka average nikalo.

## step 2: ex.: 10+10+10 = 30 len =3  average = 30/3 =10

## Step 3: pseudocode

# 1. no. ki list lo.
# 2. total = 0
# 3. list ke pure no. ko (m) bathaye 
# 4. total = total + m
# 5. avrage = total / list me pure no. kitne hai bathaye
# 6. or uska avrage nikale

## step 4: 

marks = [87, 67, 30, 67, 16]

total = 0
for m in marks:
    
    total = total + m
average = total / len(marks)

print(average)

 # Step 5:

 # step     marks       total       len
 # s 1      87            -          1
 # f-lp1    87            0          1
 # f-lp1    87            87         1
 # f-lp2    67            87         2
 # f-lp2    67            154        2
 # f-lp2    30            154        3
 # f-lp3    30            184        3
 # f-lp3    67            184        4
 # f-lp4    67            251        4
 # f-lp4    16            251        5
 # f-lp5    16            267        5
 # f-lp5    16            267        5
 # average  16            267        5
 # print(52.4)