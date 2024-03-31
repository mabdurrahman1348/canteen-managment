import officer as o
import worker as w
import file as f

def home_page():
    while True:
        print("Welcome to the Canteen Management System!")
        print("Please select an option:")
        print("1. Officer")
        print("2. Worker")
        print("3. Menu")

        option = input("Enter your choice (1 or 2 or 3): ")

        if option == '1':
            o.officer()
            break
        elif option == '2':
            w.worker()
            break
        elif option == '3':
            f.menu_file()
            break
        else:
            print('1:Invalid Input!')
            print('2:To Continue press n!')
            print('3:To exit press any other key!')
            choice = input('Enter Here: ').lower()
            if choice == 'n':
                print('')
            else:
                break