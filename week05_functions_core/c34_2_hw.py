# c34:        que 2:
## Jaan-boojh kar `def f(x=[])` waala bug banao, 3 call karke bug dikhao.

# step 1:
# Jaan-boojh kar `def f(x=[])` waala bug banao, 3 call karke bug dikhao.

# step 2:  ex.

# step 3:
# 1: def mai function mai parameter or defalt parameter do. fruits(n,p=[])
# 2: p.apend(n) append ke function mai hum no. de sakte hai.
# 3: return mai (p) do quvki hame vo (p) ki value return karega.
# 4: print mai function mai no. do 3 baar print karke.

# step 4:

def fruits(n,p=[]):
    p.append(n)
    return p

print(fruits(26))
print(fruits(16))
print(fruits(17))

# step 5:

# [26]
# [26, 16]
# [26, 16, 17]
