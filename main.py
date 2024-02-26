from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
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


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    window.config(bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")   # resetting timer text
    canvas.config(bg=YELLOW)
    title.config(text="Timer", bg=YELLOW)
    tick.config(text="", bg=YELLOW)
    global reps
    reps = 0  # this is so that reps keep increasing and it'll jump to next stage even after reset


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps += 1
    print(reps)

    # this way using modulo the program can run forever and code is short instead of what i last did reps == numbers
    if reps % 8 == 0:
        countdown(long_break_seconds)
        title.config(text="Long Break", fg=RED, bg="#A4BC92")
        window.config(bg="#A4BC92")
        canvas.config(bg="#A4BC92")
        tick.config(bg="#A4BC92")
    elif reps % 2 == 0:
        countdown(short_break_seconds)
        title.config(text="Short Break", fg=PINK, bg="#6C9BCF")
        window.config(bg="#6C9BCF")
        canvas.config(bg="#6C9BCF")
        tick.config(bg="#6C9BCF")
    else:
        countdown(work_seconds)
        title.config(text="Working time", fg=GREEN, bg="#E97777")
        window.config(bg="#E97777")
        canvas.config(bg="#E97777")
        tick.config(bg="#E97777")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_minute = math.floor(count / 60)  # returns the largest whole number less than the number if 4.8 it returns 4
    count_second = count % 60

    if count_second < 10:
        count_second = "0" + str(count_second)  # alternate way f{0 + {count_second}}

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
        # timer is global so that it can hold onto this value so and not be only a local value ( necessary for reset)
    else:
        start_timer()
        mark = ""
        work_completed = math.floor(reps / 2)

        for i in range(work_completed):
            mark += "✔"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 35, "bold"))
title.config(bg=YELLOW, fg=GREEN, pady=10)
title.grid(column=1, row=0)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_image = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(102, 112, image=pomodoro_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bd=0, width=8, font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.config(bg="#FFCDA8")
start_button.grid(column=0, row=2)

# bd=0 means no border on buttons
reset_button = Button(text="Reset", bd=0, width=8, font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.config(bg="#FFCDA8")
reset_button.grid(column=2, row=2)

tick = Label(font=(FONT_NAME, 12, "bold"))
tick.config(bg=YELLOW, fg=GREEN, pady=10)
tick.grid(column=1, row=3)

window.mainloop()
