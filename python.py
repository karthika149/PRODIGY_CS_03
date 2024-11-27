import re

def assess_password_strength(password: str) -> str:
    """
    Assess the strength of a password based on length, uppercase/lowercase letters,
    numbers, and special characters. Provides feedback for improvement.
    """
    feedback = []
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Increase the length to at least 8 characters.")

    # Check for mix of uppercase and lowercase letters
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Check for numbers
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("Add at least one numeric character.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (e.g., @, #, $, etc.).")

    # Determine overall strength
    if strength == 4:
        return "Strong password! Great job."
    elif strength == 3:
        return "Moderately strong password. Consider these improvements:\n" + "\n".join(feedback)
    elif strength == 2:
        return "Weak password. Improvements needed:\n" + "\n".join(feedback)
    else:
        return "Very weak password. Major improvements needed:\n" + "\n".join(feedback)

# User interaction
def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Enter a password to check its strength: ")
    result = assess_password_strength(password)
    print("\n" + result)

if __name__ == "__main__":
    main()
