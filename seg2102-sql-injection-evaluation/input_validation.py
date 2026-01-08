# input_validation.py
# Server-side input validation using allow-list rules

def validate_input(username, password):
    # Allow-list: username must be alphanumeric
    if not username.isalnum():
        return False

    # Length restrictions
    if len(username) > 30 or len(password) > 30:
        return False

    # Empty password check
    if password == "":
        return False

    return True
