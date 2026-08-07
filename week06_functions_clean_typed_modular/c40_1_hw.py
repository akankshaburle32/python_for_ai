# c40:      que 1:
## tools.py` mein ek aur function add karo: `is_palindrome(text: str) -> bool` (typed + docstring).

# step 1:
## tools.py` mein ek aur function add karo: `is_palindrome(text: str) -> bool` (typed + docstring).

# step 2:   ex. :  "madam" = True

# step 3:

# 1: def mai fun lo or parameter do.
# 2: isme """ sentance do """.
# 3: return mai text == text[::-1] do.
# 4: print mai fun or uski value

# step 4:

def is_palindrome(text: str) -> bool:
    
    """
        Check whether the given text is a palindrome.
        Return True if it is, otherwise False.
        
    """
    return text == text[::-1] 

print(is_palindrome("Chakuli"))    


# step 5:

"""
False

"""