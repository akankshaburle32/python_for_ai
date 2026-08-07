def add(a, b):
    return a + b

def sub(a, b):
    return a - b  

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

function_list = ["add", "sub", "multi", "div", "mod"]


if __name__ == "__main__":

    print("Testing and function: ")
    add_result = add(3, 5)
    print("addition result :", add_result)

    print("Testing and function: ")
    sub_result = sub(3, 5)
    print("subtraction result :", sub_result)

    print("Testing and function: ")
    multi_result = multi(3, 5)
    print("multiplication result :", multi_result)

    print("Testing and function: ")

    print("Testing and function: ")
    mod_result = mod(3, 5)
    print("modulus result :", mod_result)


print("======================================================================")

def is_palindrome(text: str) -> bool:
    
    """
        Check whether the given text is a palindrome.
        Return True if it is, otherwise False.
        
    """
    return text == text[::-1] 

print(is_palindrome("Chakuli"))    


print("==========================================================================")





