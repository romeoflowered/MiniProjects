from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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


entry_website = Entry(width=21, highlightbackground=WHITE)
entry_website.grid(row=1, column=1)
entry_website.focus()
entry_email_username = Entry(width=38, highlightbackground=WHITE)
entry_email_username.grid(row=2, column=1, columnspan=2)
entry_email_username.insert(0, "roma@yandex.by")
entry_password = Entry(width=21, highlightbackground=WHITE)
entry_password.grid(row=3, column=1)


search_button = Button(text="Search", highlightbackground=WHITE, width=12, command=find_password)
search_button.grid(row=1, column=2)
generate_button_button = Button(text="Generate Password", highlightbackground=WHITE,
                                width=12, command=generate_password)
generate_button_button.grid(row=3, column=2)
add_button = Button(text="Add", highlightbackground=WHITE, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
