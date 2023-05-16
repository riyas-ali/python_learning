print("LOGIN SYSTEM")

user_name = "david"
password = "privatejet"


def login():
    while True:
        login_username = input("Enter your username: ")
        login_password = input("Password: ")

        if login_username == user_name and login_password == password:
            print("Login successful, Welcome...!")
            break
        else:
            print("Whoops! I don't recognise that username or password, try again")


login()
