import string
import random

print("***Password Generator***")
char_string = string.ascii_letters + string.digits + string.punctuation
while(True):
    pwd_len = int(input("\nEnter the length of password:"))   #length of the password
    password = ""

    for i in range (pwd_len):
        random_char = random.choice(char_string)
        password += random_char
    print("Password:",password,"\n")
        
    choice_repeat = input("Do you want to continue(y/n):")
    print()
    if choice_repeat.lower() != "y":
        break

