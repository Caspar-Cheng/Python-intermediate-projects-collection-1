from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = "Calibri"


# PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # use list comprehension to create new list based on previous lists
    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    # put items in password_list randomly
    shuffle(password_list)
    random_password = "".join(password_list)
    password_input.insert(END, random_password)

    # copy the generated random password to clipboard, and it can be used by user instantly to other place
    pyperclip.copy(random_password)


# SAVE PASSWORD
def save():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please enter the required details to go next!")
    else:
        go_next = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                                f"\nPassword: {password} \nIs it ok to save?")

        if go_next:
            with open("password_data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_input.delete(0, END)
                password_input.delete(0, END)


# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=40)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website", font=(FONT, 12))
web_label.grid(column=0, row=1)
web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()

email_label = Label(text="Email/Username:", font=(FONT, 12))
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(END, "caspar@gmail.com")

password_label = Label(text="Password:", font=(FONT, 12))
password_label.grid(column=0, row=3)
password_input = Entry(width=25)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", font=(FONT, 10), command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="ADD", width=36, font=(FONT, 12, "bold"), command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
