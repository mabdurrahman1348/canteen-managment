import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Merit Pack. Ltd")
window.geometry('400x530')

bg_image = tkinter.PhotoImage(file='background.png')
background_label = tkinter.Label(window, image=bg_image)
background_label.grid(row=0, column=0, columnspan=2, pady=(0, 5))  # Reduce the top padding

def login():
    username = "admin"
    password = "admin"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid credentials.")

# Creating widgets
login_label = tkinter.Label(
    window, text="Login", fg="#013220", font=("Arial", 30))
username_label = tkinter.Label(
    window, text="Username",  fg="#013220", font=("Arial", 16))
username_entry = tkinter.Entry(window, font=("Arial", 16))
password_entry = tkinter.Entry(window, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    window, text="Password",  fg="#013220", font=("Arial", 16))
login_button = tkinter.Button(
    window, text="Login", bg="#013220", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=1, column=0, columnspan=2, pady=(2, 10))  # Adjust top padding
username_label.grid(row=2, column=0, sticky="w", padx=20)  # Align to the left
username_entry.grid(row=2, column=1, pady=10)  # Place next to the label
password_label.grid(row=3, column=0, sticky="w", padx=20)  # Align to the left
password_entry.grid(row=3, column=1, pady=10)  # Place next to the label
login_button.grid(row=4, column=0, columnspan=2, pady=(10, 20))  # Adjust bottom padding

window.mainloop()
