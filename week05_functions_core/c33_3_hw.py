# c33:    que 3:
## greet_all(*names) jo har naam ko "Hello NAME" print kare (loop se).

# step 4:

def greet_all(*names):
    for name in names:
        print(f"Hello", {name})
greet_all("Chakuli")