# c48:  que 1:
## `Date` class banao with `from_string("2026-06-28")` classmethod (year, month, day mein todo).

# step 1:
## `Date` class banao with `from_string("2026-06-28")` classmethod (year, month, day mein todo).

# step 2:

# step 3:

# 1: Date ka class lo.
# 2: def mai __init__ method lo. attribute do.
# 3: @classmethod lo usme def mai from_strings method lo usme cls, text lo.
# 4: y, m, d = text.split("-") is se gap aati hai no. ke or text ke bhi.
# 5: return mai cls(int ke 3 baar int or 3 words lokho).
# 6: Date.method mai value do.
# 7: print karo class or parameter ko.

# step 4:

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, text):
        y, m, d = text.split("-")
        return cls(int(y), int(m), int(d))

D = Date.from_string("2026-06-28")

print("===============")
print(D.year, D.month, D.day)    
print("===============")         

# step 5:

"""
===============
2026 6 28
===============

"""