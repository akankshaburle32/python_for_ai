# c54:  que 2:
## Ek custom exception `NegativeNumberError` banao aur ek function jo negative par use raise kare.

# step 1:
## Ek custom exception `## Ek custom exception `NegativeNumberError` banao aur ek function jo negative par use raise kare.

# step 2:

# step 3:

# 1: NegativeNumberError class banao. or pass.
# 2: def mai check_number ka fun lo. if mai num < 0.
# 3: raise mai error konsa vo do. raturn mai num.
# 4: try mai print mai fun lo.
# 5: except mai class mai error do.

# step 4:

class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Number negative hai")
    return num


try:
    print(check_number(-5))

except NegativeNumberError as e:
    print(f"Error : {e}")        

# step 5:

"""
Error : Number negative hai

"""