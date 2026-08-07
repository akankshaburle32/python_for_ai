"""
### Project 26 — Number Guessing Game (refactored)
- **EN:** Refactor the guessing game into functions: `check_guess(guess, secret)` returns `"low"/"high"/"correct"`, and `play(secret, max_attempts)` runs the whole game loop using it, returning `True` if the player won. Print win/lose with attempts used.
- **हिंदी:** guessing game को functions में बाँटो: `check_guess(guess, secret)` जो `"low"/"high"/"correct"` return करे, और `play(secret, max_attempts)` जो पूरा game loop चलाए और जीतने पर `True` return करे। कितने attempts लगे उसके साथ win/lose print करो।
- **Concepts:** helper functions, `while`, counter, `return` a boolean
- **Hint:** Loop `while attempts < max_attempts`; on `"correct"` return `True`; after loop return `False`

"""


def check_guess(guess, secret):
    def max_attemps():
        while secret < max_attemps:
            
            return False
    if guess > secret:
         print("high")

    elif guess < secret:
        print("low")

    else:
        print("correct")
        return True
    
print(check_guess(70, 83))


   

