import file as f
import meal as m
def worker():
    while True:
        print("1:Worker List")
        print("2:Data Entry")
        choice = input('Please Choose an option (1 or 2): ')
        if choice == '1':
            f.worker_file('worker.txt')
            break
        elif choice == '2':
            m.mark_meal("worker.txt","worker_rect.txt")
            break
        else:
            print('Invalid Input!')
            print('To Continue press n!')
            print('To exit press any other key!')
            choice = input('Enter here: ').lower()
            if choice == 'n':
                print('')
            else:
                exit()