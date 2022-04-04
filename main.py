import tkinter
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
new_text=""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global new_text
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))

    reps = 0
    new_text = ""
    check_label.config(text=new_text)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global new_text
    global reps
    # if reps == 0:
    reps += 1

    if reps in [1,3,5,7]:
            title_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 35, "bold"))
            count_down(WORK_MIN * 60)
    elif reps in [2, 4, 6]:
            new_text += "✓"
            check_label.config(text=new_text)
            title_label.config(text="Break", fg=PINK, font=(FONT_NAME, 35, "bold"))
            count_down(SHORT_BREAK_MIN * 60)
    elif reps == 8:
            new_text += "✓"
            check_label.config(text=new_text)
            title_label.config(text="Done",fg=RED , font=(FONT_NAME, 35, "bold"))
            count_down(LONG_BREAK_MIN * 60)
    else:
            title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"
    if count_min in range(0, 10):
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro timer")
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.config(padx=100, pady=50, bg=YELLOW)

start_button = tkinter.Button(text="Start", command = start_timer)
start_button.grid(column=0, row=2)
start_button.config(padx=10, pady=10)

reset_button = tkinter.Button(text="Reset", command = reset)
reset_button.grid(column=2, row=2)
reset_button.config(padx=10, pady=10)

# title_text_canvas = tkinter.Canvas(width=150, height=100, bg=YELLOW, highlightthickness=0)
# title_text_canvas.create_text(75, 50, text="Timer", fill=GREEN, font=(FONT_NAME, 35, "bold"))
# title_text_canvas.grid(column=1,row=0)
title_label= tkinter.Label(text="Timer", bg=YELLOW , fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1,row=0)
#title_label.config(padx=10, pady=10)

# ticker_canvas = tkinter.Canvas(width=50, height=50, bg=YELLOW, highlightthickness=0)
# ticker_canvas.create_text(25, 25, text="✓", fill=GREEN, font=(FONT_NAME, 16, "bold"))
# ticker_canvas.grid(column=1,row=3)
check_label= tkinter.Label(bg=YELLOW , fg=GREEN, font=(FONT_NAME, 16, "bold"))
check_label.grid(column=1,row=3)
#check_label.config(padx=10, pady=10)
#✓

canvas = tkinter.Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(105, 108, image=tomato)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



window.mainloop()