from tkinter import *
import pandas
import random

FONT = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"
card = {}

# start with the words to learn doc, if not exist, use the original words doc as data file
# choose orient=records to make the data format as {French: "", English: ""},{...},{...}...
try:
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")


# generate random word from word .csv document
def next_card():
    global card, flip_timer
    # cancel the previous window.after action
    window.after_cancel(flip_timer)
    card = random.choice(data)
    canvas.itemconfig(card_title, text="French", fill="lightgreen")
    canvas.itemconfig(card_word, text=card["French"], fill="darkorange")
    canvas.itemconfig(card_img, image=front_img)
    # recount a new flip timer for current card
    flip_timer = window.after(3000, flip_card)


# flip to the english meaning after 3 secs automatically
def flip_card():
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="lightblue")
    canvas.itemconfig(card_word, text=card["English"], fill="white")


# set the is known function to right button and delete the known words from dictionary
def word_is_known():
    data.remove(card)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv")
    next_card()


# UI setting
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(405, 270, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=(FONT, 40, "italic"), fill="lightgreen")
card_word = canvas.create_text(400, 263, text="word", font=(FONT, 60, "bold"), fill="darkorange")

right_button = Button(image=right_img, highlightthickness=0, border=0, command=word_is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, border=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
