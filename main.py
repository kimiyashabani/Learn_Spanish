from tkinter import *
import random
import json
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"


# -------------------------------- HANDLING FUNCTIONS --------------------------------
def flip_card():
    canvas.itemconfig(word, text=current_card["ENGLISH"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(card_background, image=flipped_image)


def generate_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dictionary)
    canvas.itemconfig(language, text="Spanish", fill="black")
    canvas.itemconfig(word, text=current_card["SPANISH"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    data_dictionary.remove(current_card)
    data = pandas.DataFrame(data_dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_random_word()


# -------------------------------- UI SETUP --------------------------------

window = Tk()
window.title("learn spanish with flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

cross_image = PhotoImage(file="images/wrong.png")
unknown_image = Button(image=cross_image, highlightthickness=0, command=generate_random_word)
unknown_image.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_image = Button(image=check_image, highlightthickness=0, command=is_known)
known_image.grid(row=1, column=1)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flipped_image = PhotoImage(file="images/card_back.png")

language = canvas.create_text(400, 150, text="", font=("Arial", 40, "normal"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
# -------------------------------- READ DATA FROM .CSV FILE --------------------------------

current_card = {}
data_dictionary = {}
try:
    words_to_learn_data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_to_english - Sheet1.csv")
    data_dictionary = original_data.to_dict(orient="records")
else:
    data_dictionary = words_to_learn_data.to_dict(orient="records")

generate_random_word()
window.mainloop()
