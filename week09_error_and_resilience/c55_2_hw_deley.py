# c55:  que 2:
## Backoff calculate karke print karo: 4 attempts ke liye wait times (delay=1).

# step 1:
## Backoff calculate karke print karo: 4 attempts ke liye wait times (delay=1).

# step 2:

# step 3:

# 1: deley = 1, attempts = 4 do.
# 2: for mai hum attempts ki jagah hum attempt kar dete hai.
# 3: wait_time = deley * (2 ** attempt) do.
# 4: print mai attemt or wait sec do.

# step 4:

delay = 1
attempts = 4

for attempt in range(attempts):
    wait_time = delay * (2 ** attempt)
    print(f"Attempt {attempt + 1}: wait {wait_time} seconds")
    
# step 5:

"""
Attempt 1: wait 1 seconds
Attempt 2: wait 2 seconds
Attempt 3: wait 4 seconds
Attempt 4: wait 8 seconds

"""