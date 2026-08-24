#c55:   que 2:
## `retry` mein ek case add karo jahan saare attempts fail hon — aakhri error dekho.

# step 1:
## `retry` mein ek case add karo jahan saare attempts fail hon — aakhri error dekho.

# step 2:

# step 3:

# 1: def mai retry ka fun lo. last error none do.
# 2: for mai 2nd para ki jagah attempt lo.
# 3: try mai return 1st para lo.
# 4: except mai error kya vo do. raise mai error do.
# 5: def mai task fun lo. usme raise mai error do.
# 6: try mai retry(task, value do.)
# 7: except mai error do.

# step 4:

def retry(func, max_attempts=3):
    last_error = None

    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            last_error = e
            print(f"Attempt {attempt + 1} failed")

    raise last_error


def task():
    raise ValueError("Task baar-baar fail ho raha hai")


try:
    retry(task, 3)
except Exception as e:
    print(f"Last error : {e}")

# step 5:
