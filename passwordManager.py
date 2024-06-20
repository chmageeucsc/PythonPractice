# allows text encryption
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    '''
    # automatically opens and closes file for you
    # "w" - "write" overrides file every time to write something new
    # "r" - "read" reads file, does not add or change it
    # "a" = "append" adds to the end of existing file OR creates and adds to new file (can read and write)'''
    
    with open("passwords.txt", "a") as f:
        f.write(name + "||" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("||")
            print("User:", user, "|| Password:", fer.decrypt(passw.encode()).decode())

while True:
    mode = input("Would you like to [add] a new password or [view] existing ones? Press [Q] to quit. ").lower()

    if mode == 'q':
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else: 
        print("Invalid mode.")
        continue