# c46:  que 2:
## Book class (title, author) mein _repr_ add karke 3 objects ki list print karo.

# step 1:
## Book class (title, author) mein _repr_ add karke 3 objects ki list print karo.

# step 2:

# step 3:

# 1: Book ka class banao.
# 2: def mai __init__ ki method lo. attribute lo.
# 3: def mai __repr__ lo.
# 4: return mai do.
# 5: print mai repr or value do.

# step 4:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return "Book(title = Rajasahab, author = Chakuli)"

b = Book("Rajasahab", "Chakuli")
print(repr(b))            

# step 5:

"""
Book(title = Rajasahab, author = Chakuli)

"""