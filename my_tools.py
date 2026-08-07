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
