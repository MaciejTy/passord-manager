from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import string
def password_generator():
    zestaw_znakow = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(zestaw_znakow) for _ in range(10))
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if password_entry.get() == "" and website_entry.get() == "":
        messagebox.showerror(title="No website and password",message="Please enter website and your password")
    elif password_entry.get() == "":
        messagebox.showerror(title="No password", message="Please enter your password")
    elif website_entry.get() == "":
        messagebox.showerror(title="No website", message="Please enter website")
    else:
        is_okay = messagebox.askokcancel(title=website_entry.get(), message=f"These are details entered: \nEmail: {email_entry.get()}\nPassword: {password_entry.get()} \nIs it ok to save?")
        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\f \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_str = Label(window, text="Website:")
website_str.grid(column=0, row=1)

website_entry = Entry(window, width=53)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_str = Label(window, text="Email/Username:")
email_str.grid(column=0, row=2)

email_entry = Entry(window, width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "maciejtyszczuk@gmail.com")

password_str = Label(window, text="Password:")
password_str.grid(column=0, row=3)

password_entry = Entry(window, width=34)
password_entry.grid(column=1, row=3)

generate_password = Button(window, text="Create Password", width=15, command=password_generator)
generate_password.grid(column=2, row=3)

add_button = Button(window, text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()