from tkinter import *
from tkinter import messagebox, PhotoImage
import random
import pandas

FONT_NAME = "Arial"
BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = {}

# ------------------ STEP TO THE ORIGINAL DATA ------------------------ #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# ---------------------------- IS KNOWN ------------------------------- #
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    # Saving the new DataFrame of unknown words #
    data = pandas.DataFrame(to_learn)
    # Index is set to False, because of repeating index during saving #
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- NEXT CARD ------------------------------ #

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# -------------------------- CHANGING THE CARD ------------------------ #

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# The Card Front
canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

# canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


#Button Wrong
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

#Button Right
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)


next_card()
window.mainloop()