def worker_file(post):
    with open(post,'r') as file:
        file_content = file.read()
        print(file_content)
    
def menu_file():
    with open('menu.txt','r') as file:
        file_content = file.read()
        print(file_content)

def officer_file(post):
    with open(post,'r') as file:
        file_content = file.read()
        print(file_content)