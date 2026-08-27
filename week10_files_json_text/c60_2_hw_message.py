# c60:  que 2:
## Logging se 3 messages (info, warning, error) print karo timestamps ke saath.

# step 1:
## Logging se 3 messages (info, warning, error) print karo timestamps ke saath.

# step 2:

# step 3:

# 1: import mai logging lo.
# 2: logging.basicConfig usme 3 format lo.
# 3: 3 message ko sentance mai lo.

# step 4:

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("This is an information message")
logging.warning("This is a warning message")
logging.error("This is an error message")

# step 5:

"""
2026-08-26 21:22:07,713 - INFO - This is an information message
2026-08-26 21:22:07,713 - WARNING - This is an warning message
2026-08-26 21:22:07,713 - ERROR - This is an error message

"""