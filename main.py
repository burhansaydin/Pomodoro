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
LONG_BREAK_MIN = 15
check_mark = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start():
    global reps
    reps += 1
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    work_min = WORK_MIN*60

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)

    else:
        count_down(work_min)
        timer_label.config(text="Work", fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = "0"+str(sec)
    if min < 10:
        min = "0"+str(min)

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start()
        mark = ""
        session = math.floor(reps/2)
        for i in range(session):
            mark += check_mark
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50, bg=GREEN)
window.title("Pomodoro")


canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 136, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


timer_label = Label(font=(FONT_NAME, 35, "bold"), bg=GREEN, fg=YELLOW)
timer_label.config(text="Timer")
timer_label.grid(column=2, row=0)

start_button = Button()
start_button.config(width=5, height=1, text="Start", highlightthickness=0, command=start)
start_button.grid(column=1, row=3)

reset_button = Button()
reset_button.config(width=5, height=1, text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=3, row=3)

check_marks = Label(fg=YELLOW, bg=GREEN, font=(FONT_NAME, 17))
check_marks.grid(column=2, row=4)


window.mainloop()
