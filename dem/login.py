import home as h
def validate_login(username, password):
    while username != "admin" or password != "admin":
        print("Invalid username or password")
        username = input("Enter username: ")
        password = input("Enter password: ")

    print("Login Successful. Welcome, Admin!")
    return h.home_page()