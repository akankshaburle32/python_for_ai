# c35:      que 3:
## Number guessing game ke 'compare' part ko ek function `check_guess(guess, secret)` mein nikaalo jo "low"/"high"/"correct" return kare.

# step 1:
# Number guessing game ke 'compare' part ko ek function `check_guess(guess, secret)` mein nikaalo jo "low"/"high"/"correct" return kare.

# step 2:  ex   67 > 61 = high, 61 == 61 = correct,  67 < 61 = low 

# step 3:

# 1: def mai function parameter do.
# 2: if mai guess < secret do return mai low.
# 3: elif mai guess > secret do return mai high.
# 4: else mai return mai correct.
# 5: print mai fun or usme value ise 3 baar print karo.

# step 4:

def check_guess(guess, secret):
    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "correct"
print(check_guess(90, 56))   
print(check_guess(45, 45))   
print(check_guess(23, 67))

# step 5:

# high
# corret
# low