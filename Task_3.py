import re

def assess_password_strength(password):
    strength = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'numbers': False,
        'special_characters': False
    }

    # Check password length
    if len(password) >= 8:
        strength['length'] = True

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength['uppercase'] = True

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength['lowercase'] = True

    # Check for numbers
    if re.search(r'\d', password):
        strength['numbers'] = True

    # Check for special characters
    if re.search(r'\W', password):
        strength['special_characters'] = True

    return strength

def provide_feedback(strength):
    feedback = []

    if not strength['length']:
        feedback.append('Your password should be at least 8 characters long.')

    if not strength['uppercase']:
        feedback.append('Your password should contain at least one uppercase letter.')

    if not strength['lowercase']:
        feedback.append('Your password should contain at least one lowercase letter.')

    if not strength['numbers']:
        feedback.append('Your password should contain at least one number.')

    if not strength['special_characters']:
        feedback.append('Your password should contain at least one special character.')

    return feedback

def is_password_strong(strength):
    return all(strength.values())

# Example usage
password = input('Enter your password: ')
strength = assess_password_strength(password)
feedback = provide_feedback(strength)

if is_password_strong(strength):
    print("Your password is strong.")
else:
    print("Your password is not strong. Here's the feedback:")
    for message in feedback:
        print(message)
