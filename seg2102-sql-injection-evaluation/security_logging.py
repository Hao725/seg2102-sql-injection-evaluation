# security_logging.py
# Security logging of rejected SQL injection attempts

import logging

# Configure logging
logging.basicConfig(
    filename="security.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def handle_input(username, password):
    if not validate_input(username, password):
        logging.warning("Suspicious input detected")
        print("Access denied")
        return False
    return True


# Simple validation function (used for demonstration)
def validate_input(username, password):
    if not username.isalnum():
        return False
    if len(username) > 30 or len(password) > 30:
        return False
    if password == "":
        return False
    return True
