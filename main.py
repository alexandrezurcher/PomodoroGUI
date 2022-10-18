from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global timer_label
    reps+=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN
    long_break_min = LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_min)
        timer_label = Label(text="Break", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
        timer_label.grid(column=1, row=0)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label = Label(text="Break", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=YELLOW)
        timer_label.grid(column=1, row=0)
    else:
        count_down(work_sec)
        timer_label = Label(text="WORK", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
        timer_label.grid(column=1, row=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    #Python DINAMICALLY TYPING allows do that:
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 20,"bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark_label = Label(text="✔", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

button_start = Button(text="Start", command=start_timer)

button_start.grid(column=0, row=2)

button_reset = Button(text="Reset")
button_reset.grid(column=2, row=2)


window.mainloop()

