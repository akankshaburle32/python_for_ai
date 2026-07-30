# c34:      que 3:
## Ek sentinel `_MISSING` banake ek function likho jo "given vs not given" bataye.

# step 1:
# Ek sentinel `_MISSING` banake ek function likho jo "given vs not given" bataye.

# step 2:  ex.

# step 3:

# 1: variable equal to value do._MISSING = object()
# 2: def mai hum function mai defalt parameter do. flower(Mogra=_MISSING)
# 3: return mai "not given" if mai Mogra or variable else mai f string mai "given" [Mogra]
# 4: print mai function or usme mai value 2 baar print karo 1 fun mai value nhi chihiye 2 mai value dalo.

# step 4:

_MISSING = object()
def Flower(Mogra=_MISSING): 
    return "not given" if Mogra is _MISSING else f"given: [Mogra]"

print(Flower())
print(Flower(90))    

# step 5:

# not given
# given : [Mogra]