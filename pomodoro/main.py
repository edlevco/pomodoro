
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#ffffb3"
FONT_NAME = "Courier"
work_min = 25
short_break_min = 5
long_break_min = 30
reps = 0
check_marks = ""
timer = None
times = 0

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
    
def save_time():
    global times
    global work_min
    global short_break_min
    global long_break_min

    timer_input_value = time_input.get()
    time_input.delete(0, "end")
    

    if times == 0:
        work_min = int(timer_input_value)
        minute_label.config(text="short break")
    elif times == 1:
        short_break_min = int(timer_input_value)
        minute_label.config(text="long break")
    elif times == 2:
        long_break_min = int(timer_input_value)
        time_input.destroy()
        minute_label.destroy()
        enter_btn.destroy()

    times +=1


def start_timer():
    global reps
    global work_min
    global short_break_min
    global long_break_min

    work_secs = work_min * 60
    short_break_secs = short_break_min * 60
    long_break_secs = long_break_min * 60

    reps += 1

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
tomato_img = PhotoImage(file="pomodoro/tomato.png")
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

time_input = Entry(width=10)
time_input.grid(column=0, row=0)

minute_label = Label(text = "work minutes", font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)
minute_label.place(x=0, y=40)

enter_btn = Button(text="Enter", highlightbackground = YELLOW, command=save_time)
enter_btn.place(x = 0, y= 60)

window.mainloop()