from tkinter import *


def converter():
    new_miles = float(input_user.get())
    kilometers = round(new_miles * 1.609)
    kilometer_result_label.config(text=f"{kilometers}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

#  Label
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)


#  Button
calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(column=1, row=3)

#  Enter
input_user = Entry(width=7)
input_user.grid(column=1, row=0)


window.mainloop()
