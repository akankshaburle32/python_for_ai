# c36   que 3:
## make_counter() banao jo har call per badhta no. de (clouser se).

# step 1:
# make_counter() banao jo har call per badhta no. de (clouser se).

# step 2:  ex. : 

# step 3:

# 1: def mai fun or parameter do.
# 2: count = [0] count mai kuch value nhi he isiliye zero diyha.
# 3: def mai counter fun do. count[0] += 1 badhta he no. +1 se.
# 4: return mai count aayga. or return mai counter aayga.
# 5: print karo jitne baar no. badhega.

# step 4:

def make_counter():
    count = [0]
    
    def counter():
        count[0] += 1
        return count[0]

    return counter

C = make_counter()

print(C())
print(C())
print(C())
print(C())

# step 5: 

"""
1
2
3
4

"""