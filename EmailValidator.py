# 41th github project --> Email Validator
print('----------Email Validator----------')
import re

PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def is_valid_email(email):
    return bool(PATTERN.match(email))


def main():
    email = input("Enter an email: ").strip()

    if not email:
        print("Nothing entered.")
        return

    if is_valid_email(email):
        print(f'"{email}" is a valid email.')
    else:
        print(f'"{email}" is not a valid email.')


main()