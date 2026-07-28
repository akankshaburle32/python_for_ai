# que 16:
## 1 se 10 tak saare even numbers print karo, har ek nayi line mein.
# (no input — just 1..10)

# step 1:
# 1 se 10 tak saare even numbers print karo, har ek nayi line mein.

# step 2:  ex: 2,4,6,8

# step 3: 

# 1: range mai (1, 11) likhiye.
# 2: if mai n % 2.
# or print kigiye.

# step 4:

for n in range(1, 11):
    if n % 2 == 0:
        print(n) 


# step 5:

# step       n   n % 2
# f-lp1      1     -
# if         1     1 
# f-lp2      2     1
# if         2     0
# f-lp3      3     0
# if         3     1
# f-lp4      4     1
# if         4     0
# f-lp5      5     0
# if         5     1
# f-lp6      6     1
# if         6     0
# f-lp7      7     0
# if         7     1
# f-lp8      8     1
# if         8     0
# f-lp9      9     0
# if         9     1
# f-lp10     10    1
# if         10    0
print(2, 4, 6, 8, 10)