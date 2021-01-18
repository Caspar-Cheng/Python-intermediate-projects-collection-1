from tkinter import *
import math
import tkinter.messagebox


# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# TIMER RESET
def reset_timer():
    # set button state 
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    # set reps to recount after click reset button
    global reps
    reps = 0   
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")


# TIMER MECHANISM
def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    # loop reps to +1 each time after previous timer is finished
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # provide pop up info to user
        tkinter.messagebox.showinfo(title="Break", message="Have a long break~")
        count_down(long_break_sec)
        timer_label.config(text="Break!", fg=RED)
    elif reps % 2 == 0:
        tkinter.messagebox.showinfo(title="Break", message="Take a small break~")
        count_down(short_break_sec)
        timer_label.config(text="Break~", fg=PINK)
    else:
        tkinter.messagebox.showinfo(title="Work", message="Let's start working~")
        count_down(work_sec)
        timer_label.config(text="Work")


# COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for i in range(work_session):
            marks += "✔"
        check_label.config(text=marks)


# UI SETUP, layouts should all set between window and window.mainloop()
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

start_button = Button(text="Start", width=8, command=start_timer, state="normal")
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", width=8, command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)

window.mainloop()
