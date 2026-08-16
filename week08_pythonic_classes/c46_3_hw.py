# c46:  que 1:
## 3 objects ki list banao aur print karke dekho `__repr__` kaise kaam karta hai.

# step 1:
## 3 objects ki list banao aur print karke dekho `__repr__` kaise kaam karta hai.

# step 2:

# step 3:

# 1: Movie ka class banao.
# 2: def mai __init__ method lo usme ek common word or 2 para lo. attribute lo.
# 3: def mai __repr__ ka method lo. return mai f string attribute lo.
# 4: class mai value do 3 baar alag alag valur do. 
# 5: print class karo.

# step 4:

class Movie:
    def __init__(self, horror, comedy):
        self.horror = horror
        self.comedy = comedy

    def __repr__(self):
        return f"Movie (horror = '{self.horror}', comedy = '{self.comedy}')"

M1 = Movie("Rajasahab", "Jine nhi dunga")
M2 = Movie("Nagavalli", "Tharthrat")
M3 = Movie("Pachadlela", "Khabrdaar")        

Movies = [M1, M2, M3]

print("===================================================================================================================================================================")
print(Movies)
print("===================================================================================================================================================================")

# step 5:

"""
===================================================================================================================================================================
[Movie (horror = 'Rajasahab', comedy = 'Jine nhi dunga'), Movie (horror = 'Nagvalli', comedy = 'Tharthrat'), Movie (horror = 'Pachadlela', comedy = 'Khabrdaar')]
===================================================================================================================================================================
"""