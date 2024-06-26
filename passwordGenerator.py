import random
import string
import time

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            print("New digit is", new_char)
            has_number = True
        elif new_char in special:
            print("New special is", new_char)
            has_special = True
            print("has special???", has_special, "\n\n")
        else:
            print("New letter is", new_char)

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

        # tests
        print("Password:", pwd)
        print("has number:", has_number)
        print("has special:", has_special)
        print("has meets:", meets_criteria, "\n")
        time.sleep(4)

    return pwd

min_length = int(input("Minimum length of password? "))
has_number = input("Should the password contain numbers? [y/n]: ").lower() == "y"
has_special = input("Should the password contain special characters? [y/n]: ").lower() == "y"

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)