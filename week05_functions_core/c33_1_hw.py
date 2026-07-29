# c33:      que 1:
## multiply_all(*nums) jo saare numbers ka product return kare.

# step 4:

def multiply_all(*nums):
    multiple_result = 1
    for n in nums:
        multiple_result = multiple_result * n
    return multiple_result
print(multiply_all(3, 6, 9))

