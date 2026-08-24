# que 20:

"""
### Project 20 — Build Your First Tools Library (capstone)
- **EN:** Create a file `my_tools.py` with 4 reusable functions, each returning a value: `celsius_to_f(c)`, `bmi(weight, height)`, `is_prime(n)`, and `word_count(text)`. Test all four and print the results. This is the seed of your own "AI tools" library!
- **हिंदी:** एक file `my_tools.py` बनाओ जिसमें 4 reusable functions हों, हर एक value **return** करे: `celsius_to_f(c)`, `bmi(weight, height)`, `is_prime(n)`, और `word_count(text)`। चारों को test करके results print करो। यह आपकी अपनी "AI tools" library की शुरुआत है!
- **Concepts:** multiple functions, `return`, loops/flags inside functions, `.split()`
- **Hint:** For `is_prime`, use a flag: assume prime, loop `2..n-1`, if any divides evenly set flag `False`. For `word_count`, `return len(text.split())`.

"""

# step 1:
# ek file "my_tools.py" banao jisme 4 reusable functions ho, har ek value **return** kare. "celsius_to_f(c)" "bmi(weight, height)" "is_prime(n)" or "word_count(text)" . charo ko test karke results print karo. yah aapki apni "AI tools" library ki shuruaat hai.

# step 2:   

# step 3:

# 1: def mai 4 fun dene hai. pahile celcius_of _f(c) return mai formula.
# 2: dusra bmi(weight, height) return mai formula.
# 3: tisra prime no. nikalana hai prime hua to True nhi hua to false. n % i == 0  >> i mean no.
# 4: fourth mai word fun mai kitne word he vo check karna hai. 

# step 4:

def celsius_to_f(c):
    return (c * 9/5) + 32

def bmi(weight, height):
    return weight / height ** 2

def is_prime(n):
    if n < 2:
        return False
    prime = True
    for i in range (2, n):
        if n % i == 0:
            prime = False 
            break 
    return prime
       
def word_count(test):
    return len(test.split())

print(celsius_to_f(100))
print(bmi(42, 5.2))
print(is_prime(26))
print(word_count("My time is Coming"))

# step 5:

"""
212.0
1.5532
False
4

"""