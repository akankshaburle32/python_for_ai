# c37:  que 1:
# Recursion se 5 se 1 tak coundown karo.

# step 1:
# Recursion se 5 se 1 tak coundown karo.

# step2:  ex:  que mai jo no. hai. us no. ko reverse karna jeseki (5, 4, 3, 2, 1)

# step 3:

# 1: def mai function mai (n) do.
# 2: print mai (n) likho. 
# 3: if mai n equal to equal to 1 do.
# 4: print mai count compled likho.
# 5: return likho.
# 6: countdown (n-1).
# 7: print mai countdown mai 5 likho quki hame 5 ka countdown karna hai. 

# step 4:

def countdown(n):
    print(n)

    if n == 1:
        print("Count Completed")
        return

    countdown(n-1)

(countdown(5))    

# step 5:

# 5
# 4
# 3
# 2
# 1
# count completed