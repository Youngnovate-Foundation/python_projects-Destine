import secrets
import string
import random


def main():
    while True:
        try:
            length = int(input("Enter your desired password length:\n"))

            while True:
                include_special_chars = (
                    input("Include special characters?\n'Yes' or 'No'\n")
                    .strip()
                    .lower()
                )
                if include_special_chars in ["yes", "no"]:
                    break
                else:
                    print("Please enter either 'Yes' or 'No'.")

        except ValueError:
            print("🚫Invalid length. Please enter a number.")
            continue
        break
    print(generate_password(length, include_special_chars))


def generate_password(length, include_special_chars):
    password_length = length
    special_chars = include_special_chars

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if special_chars == "yes":
        all_chars = lower + upper + digits + symbols
        password_list = [
            secrets.choice(lower),
            secrets.choice(upper),
            secrets.choice(digits),
            secrets.choice(symbols),  # include symbol only if yes
        ]
    elif special_chars == "no":
        all_chars = lower + upper + digits
        password_list = [
            secrets.choice(lower),
            secrets.choice(upper),
            secrets.choice(digits),
        ]

    # Fill remaining characters
    password_list += [
        secrets.choice(all_chars) for _ in range(password_length - len(password_list))
    ]

    random.shuffle(password_list)

    user_password = ""
    for char in password_list:
        user_password += char

    return f"Your Password: {user_password}"


if __name__ == "__main__":
    main()
