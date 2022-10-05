from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
BLACK_COLOR = "#000000"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/1000_english_words .csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill=BLACK_COLOR)
    canvas.itemconfig(card_word, text=current_card["English"], fill=BLACK_COLOR)
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Russian", fill="white")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


red_buttons_img = PhotoImage(file="images/wrong.png")
red_buttons = Button(image=red_buttons_img, highlightthickness=0,
                     highlightbackground=BACKGROUND_COLOR, command=next_card)
red_buttons.grid(row=1, column=0)

green_buttons_img = PhotoImage(file="images/right.png")
green_buttons = Button(image=green_buttons_img, highlightthickness=0,
                       highlightbackground=BACKGROUND_COLOR, command=is_known)
green_buttons.grid(row=1, column=1)


next_card()


window.mainloop()
