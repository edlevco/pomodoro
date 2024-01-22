
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#ffffb3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
check_marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    global check_marks
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks = 0
    reps = 0
    



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_secs)
        timer_label.config(text = "Work", fg=GREEN)
    if reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text = "SHORT BREAK", fg=PINK)
    if reps == 8:
        count_down(long_break_secs)
        timer_label.config(text = "Long Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_marks

    minutes = count // 60
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    if minutes < 10:
        minutes = f"0{minutes}"


    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        if reps & 2 == 0:
            check_marks += "✔"
            check_mark_text.config(text=check_marks)


        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx = 100, pady=50)
window.config(bg=YELLOW)
window.minsize(width = 500, height = 400)





canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row = 1)



timer_label = Label(text="Timer", font = (FONT_NAME, 40, "bold"), fg=GREEN, bg = YELLOW)
timer_label.grid(column=1, row = 0)

start_btn = Button(text="Start", highlightbackground = YELLOW, command=start_timer)
start_btn.grid(column = 0, row = 2)

reset_btn = Button(text="Reset", highlightbackground = YELLOW, command=reset_timer)
reset_btn.grid(column = 2, row = 2)

check_mark_text = Label(text="", font = (FONT_NAME, 25, "bold"), fg=GREEN, bg = YELLOW)
check_mark_text.grid(column = 1, row = 3)



window.mainloop()