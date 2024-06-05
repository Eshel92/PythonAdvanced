import string

class UsernameContainsIllegalCharacter(Exception):
    """
    Exception raised for usernames containing illegal characters.

    Attributes:
        illegal_char (str): The illegal character found in the username.
        index (int): The index of the illegal character in the username.
    """
    def __init__(self, illegal_char, index):
        self.illegal_char = illegal_char
        self.index = index

    def __str__(self):
        return f"The username contains an illegal character '{self.illegal_char}' at index {self.index}"


class UsernameTooShort(Exception):
    """Exception raised for usernames that are too short."""
    def __str__(self):
        return "Username is too short"

class UsernameTooLong(Exception):
    """Exception raised for usernames that are too long."""
    def __str__(self):
        return "Username is too long"

class PasswordMissingCharacter(Exception):
    """Exception raised for passwords missing required characters."""
    def __str__(self):
        return "Password is missing required character"

class PasswordTooShort(Exception):
    """Exception raised for passwords that are too short."""
    def __str__(self):
        return "Password is too short"

class PasswordTooLong(Exception):
    """Exception raised for passwords that are too long."""
    def __str__(self):
        return "Password is too long"

class PasswordMissingUppercase(PasswordMissingCharacter):
    """Exception raised for passwords missing an uppercase character."""
    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    """Exception raised for passwords missing a lowercase character."""
    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    """Exception raised for passwords missing a digit."""
    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    """Exception raised for passwords missing a special character."""
    def __str__(self):
        return super().__str__() + " (Special)"


def check_input(username, password):
    """
    Validates the given username and password.
    """
    valid_chars = string.ascii_letters + string.digits + "_"
    special_chars = set(string.punctuation)

    # Check username
    for index, char in enumerate(username):
        if char not in valid_chars:
            raise UsernameContainsIllegalCharacter(char, index)
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()

    # Check password
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_chars for char in password)

    if not has_upper:
        raise PasswordMissingUppercase()
    if not has_lower:
        raise PasswordMissingLowercase()
    if not has_digit:
        raise PasswordMissingDigit()
    if not has_special:
        raise PasswordMissingSpecial()
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()

    print("OK")

def main():
    """
    Main function to get user input for username and password,
    and validate them using the check_input function.

    Continues to prompt the user until valid input is provided.
    """
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            check_input(username, password)
            break  # Exit loop if input is valid
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
