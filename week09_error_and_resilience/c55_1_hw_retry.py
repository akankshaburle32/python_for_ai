# c55:  que 1:
## `retry` function ko ek aise task par chalao jo pehle 2 baar fail kare phir success de.

# step 1:
## `retry` function ko ek aise task par chalao jo pehle 2 baar fail kare phir success de.

# step 2:

# step 3:

# 1: def mai retry fun do or usme para do.
# 2: for mai range do usme 2nd para do.
# 3: try mai return 1st para. do .
# 4: except mai error konsa hai vo do.
# 5: count = 0 lo. def mai task ka fun banao. global count lo.
# 6: count add 1 . if mai count < 3 karo or raise mai ValuError do print mai Task Failed.
# 7: return mai Task Successfull do print mai 1st fun mai 2nd fun.

# step 4:

def retry(func, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed")

    print("All attempts failed")


count = 0

def task():
    global count
    count += 1

    if count < 3:
        raise ValueError("Task failed")

    return "Task successful!"


print(retry(task))

# step 5:

"""
Attempt 1 failed
Attempt 2 failed
Task successfull

"""