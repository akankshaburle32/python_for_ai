# c34:      que 1:
## `add_to_list` likho jo default `None` use kare, 3 alag baar call karke dikhao har baar fresh list aati hai.

# step 1:
# `add_to_list` likho jo default `None` use kare, 3 alag baar call karke dikhao har baar fresh list aati hai.

# step 2:   ex. 

# step 3:

# 1: def mai function do or usme parameter or defalt parameter dalo. (apple, red=None)
# 2: hum red ke badleme None likh sakte hai.
# 3: red equal to dic de sakte hai.
# 4: red.append function mai hum apple dal sakte hai.
# 5: return mai hum, red de sakte hai.
# 6: print mai function("a") de sakte hai, print mai function mai("b"), print mai function mai("c").

# step 4:

def add_to_list(apple, red=None):
    if red is None:
        red = []
        red.append(apple)
        return red

print(add_to_list("a"))
print(add_to_list("b"))
print(add_to_list("c"))

# step 5:

# ['a']
# ['b']
# ['c']