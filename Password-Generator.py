# ------------------ PASSWORD GENERATOR PROGRAM ------------------
# Author: Honu K. Destine
# Description: A secure password generator that allows users to
# specify password length and choose whether to include special characters.
# and then displays generated password to user
# -----------------------------------------------------------------


# for secure random character selection
import secrets

# provides sets of characters (letters, digits, punctuations/symbols)
import string

# for randomly shuffling generated password characters
import random


# main() function to start program
def main():
    # prints the final generated password returned from user_input() function
    print(user_input())


# to take user inputs specification for password length and structure
def user_input():
    # initializes a loop to keep prompting user for correct input
    while True:
        try:
            # prompt user to input desired password length
            length = int(input("Enter your desired password length:\n"))

            # keep prompting until user enters either 'yes' or 'no'
            while True:
                include_special_chars = (
                    input("Include special characters?\n'Yes' or 'No'\n")
                    .strip()
                    .lower()
                )
                # accept valid response
                if include_special_chars in ["yes", "no"]:
                    break
                # otherwise warn and prompt again
                else:
                    print("Please enter either 'Yes' or 'No'.")

        except ValueError:
            # Re-prompt if length is not a non-numeric
            print("🚫Invalid length. Please enter a number.")
            continue
        # if nothing goes wrong, break out of the loop
        break
    #  and then pass inputs to the generate_password() function and return the result
    return generate_password(length, include_special_chars)


# generate password using random selections from chosen character sets
# includes lowercase, uppercase, digits and symbol(if chosen)
def generate_password(length, include_special_chars):

    # Character sets
    lower = string.ascii_lowercase  # lowercase characters
    upper = string.ascii_uppercase  # uppercase characters
    digits = string.digits  # digits
    symbols = string.punctuation  # symbols

    # determine characters to use based on what the user chooses
    if include_special_chars == "yes":
        all_chars = lower + upper + digits + symbols
        password_list = [
            secrets.choice(lower),
            secrets.choice(upper),
            secrets.choice(digits),
            secrets.choice(symbols),  # include symbol only if yes
        ]

    # do not add symbols if user choice is "no"
    elif include_special_chars == "no":
        all_chars = lower + upper + digits
        password_list = [
            secrets.choice(lower),
            secrets.choice(upper),
            secrets.choice(digits),
        ]

    # Add random characters to meet the desired length
    password_list += [
        secrets.choice(all_chars) for _ in range(length - len(password_list))
    ]

    # Shuffle the list to so that the sequence don't stay the same
    random.shuffle(password_list)

    # Now with the characters in the list, generate a password
    # By looping through the list
    user_password = ""
    for char in password_list:
        user_password += char

    # Just a summary to user showing the choice the made
    print(f"Length: {length} | Special characters: {include_special_chars.title()}")

    # Return the formatted final password string
    return f"Your Password: {user_password}"


# Program entry point
if __name__ == "__main__":
    main()
