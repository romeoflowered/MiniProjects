from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

WHITE = "#ffffff"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg=WHITE)
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/UserName:", bg=WHITE)
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=WHITE)
password_label.grid(row=3, column=0)


entry_website = Entry(width=38, highlightbackground=WHITE)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
entry_email_username = Entry(width=38, highlightbackground=WHITE)
entry_email_username.grid(row=2, column=1, columnspan=2)
entry_email_username.insert(0, "roma@yandex.by")
entry_password = Entry(width=21, highlightbackground=WHITE)
entry_password.grid(row=3, column=1)


generate_button_button = Button(text="Generate Password", highlightbackground=WHITE,
                                width=12, command=generate_password)
generate_button_button.grid(row=3, column=2)
add_button = Button(text="Add", highlightbackground=WHITE, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
