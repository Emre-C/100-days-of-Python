BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

x_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)
check_button = Button(image=right_img, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)


window.mainloop()