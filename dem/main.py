import login as l
def main():
    print("Canteen Management System Login")

    username = input("Enter username: ")
    password = input("Enter password: ")

    l.validate_login(username, password)


main()