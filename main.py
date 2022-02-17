from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    file = pandas.read_csv("data/words_to_learn.csv")
except:
    file = pandas.read_csv("data/french_words.csv")
finally:
    data = file.to_dict(orient="records")


def english_word():
    global current_card
    current_card = random.choice(data)
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(background, image=back_image)


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(background, image=front_image)
    flip_timer = window.after(3000, english_word)


def know_the_word():
    data.remove(current_card)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Canvas
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=know_the_word)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(column=1, row=1)

flip_timer = window.after(3000, english_word)
next_card()

window.mainloop()
