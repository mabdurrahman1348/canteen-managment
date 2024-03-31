import datetime as dt
now = dt.datetime.now()


def mark_meal(post1,post2):
    print('Do you want to enter meal record? (y/n)')
    ans = input('Your answer here: ')
    if ans == 'y':
        num = input('Enter the employee number: ')
        with open(post1,'r') as file:
            lines = file.readlines()
            mod_lines = [line.strip().split(':') for line in lines]
            for i in range(len(lines)):
                info = mod_lines[i][0]
                if num == info:
                    with open(post2,"r") as file:
                        rec_lines = file.readlines()
                        rec_lines[i] = rec_lines[i].strip() + ':'+ now.strftime('%d-%m-%y')+'\n'
                    with open(post2,"w") as file:
                        file.writelines(rec_lines)