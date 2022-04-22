import re
import json

def read_from_file():
    with open('database.json', 'r') as file:
        return json.load(file)

def write_to_file(user):
    data = read_from_file()
    data.update(user)
    with open('database.json', 'w') as file:
        json.dump(data, file)

def login():
    email = input("Enter your email:")
    data = read_from_file()
    if email in data.keys():
        password = input("Enter your password:")
        if data[email] == password:
            print("Login Successful")
        else:
            print("Invalid password")
    else:
        print("User does not exsist please create account")
        registration()
        


def registration():
    regex = r'\b[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'

    while True:     
        email= input("create username(eg- abc@gmail.com):")
        if(re.fullmatch(regex, email)):
            print("Valid Email")
            final_email = email
            break
        else:
            print("Invalid Email")

    while True:
        password = input("enter password password:")
        temp = 0
        if len(password) < 5 or len(password)>16:
            print("please enter password between 5 and 16 charachters")
            temp = temp + 1
        if not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            temp = temp + 1
            
        if not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter')
            temp = temp + 1
            
        if not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter')
            temp = temp + 1

        if not any(char in ['$', '@', '#', '%'] for char in password):
            print('Password should have at least one of the symbols $@#')
            temp = temp + 1
        
        if temp == 0:
            final_password = password
            break

    if final_email and final_password:
        write_to_file({final_email:final_password})
        print("User created successfully")

def login_or_register():
    print("1. Login")
    print("2. Register")
    choice = input("Enter your choice:")
    if choice == '1':
        login()
    elif choice == '2':
        registration()
    else:
        print("Invalid choice")
        login_or_register()


login_or_register()
            