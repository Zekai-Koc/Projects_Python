# This app's created for educational purposes. It is a GUI oriented app and uses many different libraries.
# It is based on the course given by Clarusway.
# Used compiler: Python 3.8.2
# Imported libraries: os, tkinter, math, time, random and windsound.
# This is a simple "catch the circle on the screee" game.  
# Bresenham's line algorithm implemented in Python.
# For detailed information please visit www.clarusway.com


import os
from tkinter import Canvas, messagebox, Tk, Button, Menu, Label, Scale, SUNKEN, HORIZONTAL, RAISED, VERTICAL
from math import sqrt, hypot
import time
import random
import winsound


clear = lambda: os.system('cls')
clear()

window_main=Tk()
window_main.resizable(0, 0)

# screen_with_org = window_main.winfo_screenwidth()
# screen_height_org = window_main.winfo_screenheight()
# screen_resolution = (screen_with_org, screen_height_org)
# screen_width_and_height = ((screen_with_org // 2), (screen_height_org // 2))

screen_width = 1007
screen_height = 622
screen_resolution = (screen_width, screen_height)   # Golden Ratio
main_window_dimensions = str(screen_resolution[0])+'x'+str(screen_resolution[1])
window_main.geometry(main_window_dimensions)
window_main.title("A Simple Game Demo App. with tkinter (click on the ball for getting points. Double click = COMBO - *3 points)...                    (created with Python 3.8)")

canvas_with = screen_resolution[0] - 25
canvas_height = screen_resolution[1] - 110
canvas_resolution = (canvas_with, canvas_height)
canvas_main=Canvas(window_main, width=canvas_with, height=canvas_height, relief=SUNKEN, bg="grey")
canvas_main.grid(row=0, column=0, columnspan=40, padx=10, pady=10)

text_status_bar = "Clarusway: Your expedition to success "
text_status_bar += "and a new way to reinvent yourself in the IT age..."
text_status_bar += "                                           "
text_status_bar += "                                           "
text_status_bar += "www.clarusway.com"

current_x_position = canvas_resolution[0] // 2
current_y_position = canvas_resolution[1] // 2

target_x_position = 0
target_y_position = 0

continue_bouncing = False
total_single_click = 0
total_double_click = 0
# final_score = 0
num_of_bouncing_circles = 1

delay_ratio = 100
delay_time = 1 / (50 * delay_ratio) # 50 comes from the scale widget's default value

def start_bouncing(): 
    global continue_bouncing 
    continue_bouncing = True
    game_loop()

def stop_bouncing(): 
    global continue_bouncing 
    continue_bouncing = False
    game_loop()

def set_new_difficulty_level(arg_from_widget):
    global delay_time
    delay_time = 1 / (int(arg_from_widget) * delay_ratio)

def game_loop():
    global target_x_position
    global target_y_position
    while continue_bouncing:
        target_x_position = random.randint(0, canvas_resolution[0])
        target_y_position = random.randint(0, canvas_resolution[1])
        plotLine()

# Bresenham's line algorithm
def plotLine():
    global current_x_position
    global current_y_position
    global target_x_position
    global target_y_position

    print(current_x_position, current_y_position, target_x_position, target_y_position)

    dx =  abs(target_x_position-current_x_position)  
    if (current_x_position<target_x_position): sx = 1
    else: sx = -1

    dy = -abs(target_y_position-current_y_position)
    if (current_y_position<target_y_position): sy = 1
    else: sy = -1
    
    err = dx+dy

    temp_x = current_x_position
    temp_y = current_y_position

    while True:
        if (current_x_position==target_x_position and current_y_position==target_y_position): 
            break

        e2 = 2*err        
        
        if (e2 >= dy): 
            err += dy
            current_x_position += sx
        
        if (e2 <= dx): 
            err += dx
            current_y_position += sy

        label_info.configure(text="Pos.X: " + str(current_x_position) + " Pos.Y: " + str(current_y_position))
        canvas_main.move(shape_oval, current_x_position - temp_x, current_y_position - temp_y)
        label_info.update()
        canvas_main.configure(bg="grey")
        time.sleep(delay_time)

        temp_x = current_x_position
        temp_y = current_y_position

button_start = Button(window_main, text="Start", font=("arial", 14, "bold"), command = start_bouncing)
button_start.grid(row=1, column=0, padx=10)

button_stop = Button(window_main, text="Stop", font=("arial", 14, "bold"), command = stop_bouncing)
button_stop.grid(row=1, column=1)

scale_difficulty_level = Scale(window_main, orient=HORIZONTAL, label="Difficulty Level:", length=250, from_=1.0, to=100.0, sliderrelief=RAISED, command=set_new_difficulty_level)
scale_difficulty_level.grid(row=1, column=2)
scale_difficulty_level.set(50)

label_info = Label(window_main, text="Pos.X: " + str(current_x_position) + " Pos.Y: " + str(current_y_position), font=("arial", 10), relief=SUNKEN)
label_info.grid(row=1, column=5)

label_single_click = Label(window_main, text="Single: ", font=("arial", 10), relief=SUNKEN)
label_single_click.grid(row=1, column=10)

label_double_click = Label(window_main, text="Double: ", font=("arial", 10), relief=SUNKEN)
label_double_click.grid(row=1, column=15)

label_final_score = Label(window_main, text="Final Score: ", font=("arial", 12, "bold"), relief=SUNKEN)
label_final_score.grid(row=1, column=20)

shape_oval = canvas_main.create_oval(current_x_position + 25, current_y_position + 25, current_x_position + 50, current_y_position + 50, width=5, fill="red", tags="oval")

scale_number_of_bouncing_circles = Scale(window_main, orient=VERTICAL, label="Ball number", length=50, from_=1, to=5, sliderrelief=SUNKEN)  # command=change_the_number_of_bouncing_circles)
scale_number_of_bouncing_circles.grid(row=1, column=38)
scale_number_of_bouncing_circles.set(3)
scale_number_of_bouncing_circles.configure(state='disabled')

scale_ball_size = Scale(window_main, orient=VERTICAL, label="Ball size", length=50, from_=1, to=5, sliderrelief=SUNKEN) 
scale_ball_size.grid(row=1, column=39)
scale_ball_size.set(3)
scale_ball_size.configure(state='disabled')

label_status_bar = Label(window_main, text=text_status_bar, font=("arial", 10), relief=SUNKEN)
label_status_bar.grid(row=2, column=0, columnspan=40)

def calculate_final_score_str():
    final_score = total_single_click + (total_double_click * 3)
    return str(final_score)

def clicked_single(*args):
    global total_single_click
    if continue_bouncing:
        winsound.Beep(400, 40)  # Beep at 400 Hz for 40 ms
        total_single_click += 1
        label_single_click.configure(text="Single: " + str(total_single_click))
        label_final_score.configure(text="Final Score: " + calculate_final_score_str())

def clicked_double(*args):
    global total_double_click
    if continue_bouncing:
        winsound.Beep(800, 40)  # Beep at 800 Hz for 40 ms
        total_double_click += 1    
        label_double_click.configure(text="Double: " + str(total_double_click))
        label_final_score.configure(text="Final Score: " + calculate_final_score_str())

canvas_main.tag_bind(shape_oval, "<Button-1>", clicked_single)
canvas_main.tag_bind(shape_oval, "<Double-1>", clicked_double)

def show_info():
    messagebox.showinfo("information","Simple game created with Python. (c)Clarusway") 

def show_warning():
    messagebox.showwarning("warning",text_status_bar)  

def show_error():
    messagebox.showerror("error","Just for testing...")  

def show_ask_question():
    messagebox.askquestion("Confirm","Just for testing...?") 

def show_cancel():
    messagebox.askokcancel("Redirect","Redirecting you to www.clarusway.com")   

def show_yes_no():
    messagebox.askyesno("Application","Just for testing...") 

def show_try_again():
    messagebox.askretrycancel("Application","Just for testing...") 

menu_bar = Menu(window_main)

menu_file = Menu(menu_bar, tearoff=0)
menu_file.add_command(label="New", command=show_error)
menu_file.add_command(label="Open", command=show_error)
menu_file.add_command(label="Save", command=show_error)
menu_file.add_command(label="Save as...", command=show_error)
menu_file.add_command(label="Close", command=show_ask_question)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=window_main.quit)
menu_bar.add_cascade(label="File", menu=menu_file)

menu_edit = Menu(menu_bar, tearoff=0)
menu_edit.add_command(label="Undo", command=show_cancel)
menu_edit.add_separator()
menu_edit.add_command(label="Cut", command=show_yes_no)
menu_edit.add_command(label="Copy", command=show_yes_no)
menu_edit.add_command(label="Paste", command=show_yes_no)
menu_edit.add_command(label="Delete", command=show_warning)
menu_edit.add_command(label="Select All", command=show_error)
menu_bar.add_cascade(label="Edit", menu=menu_edit)

menu_help = Menu(menu_bar, tearoff=0)
menu_help.add_command(label="Help Index", command=show_try_again)
menu_help.add_command(label="About...", command=show_info)
menu_bar.add_cascade(label="Help", menu=menu_help)

window_main.config(menu=menu_bar)


window_main.mainloop()