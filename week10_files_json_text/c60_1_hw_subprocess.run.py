# c60:  que 1:
## `subprocess.run` se `python --version` chalao (list form) aur output print karo.

# step 1:
## `subprocess.run` se `python --version` chalao (list form) aur output print karo.

# step 2:

# step 3:

# 1: import mai subprocess lo.
# 2: result mai subprocess.run python version do.
# 3: print mai result.stdout lo.

# step 4:

import subprocess

result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print(result.stdout)

# step 5:

"""
Python 3.14.6

"""