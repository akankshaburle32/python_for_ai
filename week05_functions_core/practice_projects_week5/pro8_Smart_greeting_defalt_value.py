# que 8:

"""
### Project 8 — Smart Greeting (default value)
- **EN:** Write `greet(name, greeting="Hello")` where `greeting` has a default. Call it once with only a name, and once with a custom greeting like `"Namaste"`.
- **हिंदी:** `greet(name, greeting="Hello")` बनाओ जिसमें `greeting` का default हो। इसे एक बार सिर्फ़ name के साथ, और एक बार custom greeting जैसे `"Namaste"` के साथ call करो।
- **Concepts:** default parameter value
- **Hint:** `return f"{greeting}, {name}!"`. Calling `greet("Asha")` uses the default.

"""

# step 1:
## "greet(name, greeting="Hello")" banao jisme greeting ka default ho. ise ek baar sirf name ke saath, or ek baar custom greeting jeise "Namaste" ke saath call karo. 

# step 2: 

# step 3:

# 1: def mai fun or usme parameter and defalt parameter do.
# 2: return main f string mai do parameter do.
# 3: print mai fun or usme name do.

# step 4:

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Chakuli"))

# step 5:

"""
Hello, Chakuli!

"""