def name_validation(name):
    if name.isspace() or not name:
        return False

    for c in name:
        if not c.isalpha() and not c.isspace():
            return False

    return True

def string_validation(sentence):
    if not sentence:
        return False
    if isinstance(sentence, str):
        for c in sentence:
            if not (c.isalpha() or c.isspace()):
                return False
        
        return True
    else:
        return False

def int_validation(value):
    try:
        int_value = int(value)
        return True
    except ValueError:
        return False

def int_validation_with_limits(value, lower_limit, upper_limit):
    try:
        int_value = int(value)
        return lower_limit <= int_value <= upper_limit
    except ValueError:
        return False
    
def password_validation(password):
    has_symbol = False
    has_letter = False
    has_digit = False

    for c in password:
        if not c.isalnum():
            has_symbol = True
        elif c.isalpha():
            has_letter = True
        elif c.isdigit():
            has_digit = True
    if has_digit and has_letter and has_symbol and len(password) > 5:
        return True
    else:
        return False

