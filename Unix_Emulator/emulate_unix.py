# Created on gihHub.

import os
import os.path
from tkinter import *
from math import sqrt, hypot
import time
import random
import winsound
from datetime import date, datetime



clear = lambda: os.system('cls')
clear()


window_main=Tk()
window_main.resizable(0, 0)

# screen_with_org = window_main.winfo_screenwidth()
# screen_height_org = window_main.winfo_screenheight()
# screen_resolution = (screen_with_org, screen_height_org)

screen_width = 1007
screen_height = 622
screen_resolution = (screen_width, screen_height)   # Golden Ratio

main_window_dimensions = str(screen_resolution[0])+'x'+str(screen_resolution[1])
window_main.geometry(main_window_dimensions)
window_main.title("A simple unix emulator for windows pc's. created with python 3.8.2.   Clarusway - ZK")


def reply(name):
    command_output_display.insert(END, "COMMAND:   " + name + "\n------------------------------\n")
    user_entry.delete(0, END)
    parse_the_command(name)
    command_output_display.see(END)


user_entry = Entry(window_main, fg="white", bg="black", insertbackground='white', width=110, font=("arial", 12))
user_entry.bind("<Return>", (lambda event: reply(user_entry.get())))
user_entry.pack()
user_entry.focus_set()


command_output_display = Text(window_main, fg="white", bg="black", width=110, height=(screen_height - 590), font=("arial", 12))
command_output_display.pack()




def parse_the_command(name):
    if name == "exit":
        window_main.quit()
    elif name == "clear":
        CLEAR_the_command_out_display()
    elif name == "pwd":
        PWD_print_working_directory(name)
    elif name == "ls":
        LS_list_files_and_folders(name)
    elif name == 'name':
        NAME_os_name()
    elif name == 'dirinfo':
        DIRINFO_dir_info()
    elif name == 'date':
        DATE_info()
    elif name == "time":
        TIME_info()
    else:
        command_output_display.insert(END, "!!! invalid command !!!\n")

    command_output_display.insert(END, "\n")
    

def CLEAR_the_command_out_display():
    command_output_display.delete("1.0", END)

def PWD_print_working_directory(name):
    # path = '.'
    # command_output_display.insert(END, "os.path.dirname(path) = " + os.path.dirname(path) + "\n")
    # path = os.getcwd()
    # command_output_display.insert(END, "os.getcwd() = " + os.path.dirname(path) + "\n")
    # path = os.path.abspath('.')
    command_output_display.insert(END, os.path.abspath('.'))


def LS_list_files_and_folders(name):
    dir_list = os.listdir()
    for i in range(len(dir_list)):
        command_output_display.insert(END, dir_list[i] + "\n")


def NAME_os_name():
    command_output_display.insert(END, "Name of the Operation System: " + os.name)

def DIRINFO_dir_info():
    print("will be checked...")
    # command_output_display.insert(END, "os.pardir: " + os.pardir)
    # command_output_display.insert(END, "os.getcwd: " + os.getcwd)
    # command_output_display.insert(END, "os.path.join(path, os.pardir) : " + os.path.join(path, os.pardir) )
    # command_output_display.insert(END, "os.path.abspath(parent): " + os.path.abspath(parent))
    # command_output_display.insert(END, "os.path.relpath(parent): " + os.path.relpath(parent))

def DATE_info():
    today = date.today()
    command_output_display.insert(END, "date.today(): " + today.strftime("%d/%m/%Y") + '\n')
    command_output_display.insert(END, "date.today(): " + today.strftime("%B %d, %Y") + '\n')
    command_output_display.insert(END, "date.today(): " + today.strftime("%m/%d/%y") + '\n')
    command_output_display.insert(END, "date.today(): " + today.strftime("%b-%d-%Y") + '\n')

def TIME_info():
    now = datetime.now()
    command_output_display.insert(END, "datetime.now(): " + str(now) + '\n')
    command_output_display.insert(END, "datetime.now(): " + now.strftime("%d/%m/%Y %H:%M:%S") + '\n')



window_main.mainloop()