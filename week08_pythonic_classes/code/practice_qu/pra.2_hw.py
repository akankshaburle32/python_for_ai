# que 2: 
## Library class banao jo Book aur Author objects rakhe (composition).

# step 1:
## Library class banao jo Book aur Author objects rakhe (composition).

# step 2: 

# step 3:

# 1: Book ka class banao usme def mai __init__ method lo. attribute lo.
# 2: Author ka class banao usme def mai __init__ method lo. attribute lo.
# 3: Library ka class banao def mai __init__ method lo. aatritribute do usme value do.
# 4: print mai class or object lo

# step 4:

class Book:
    def __init__(self, title):
        self.title = title

class Author:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.book = Book("Story Book")
        self.author = Author("R. K. Narayan")

Library = Library()

print("-----------------")
print(Library.book.title)
print(Library.author.name)
print("-----------------")

# step 5:

"""
-------------------
Story Book
R. K Narayan
-------------------

"""
