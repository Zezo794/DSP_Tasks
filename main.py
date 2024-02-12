from GlobalFunctions import *
from Task2 import *
from Task3 import *
from Task4_5 import *
from tkinter import *
from functools import partial
from task6_7 import *
from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button, Frame
from Task1 import *

# Create window and set the position
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (600 / 2))
y = int((screen_height / 2) - (700 / 2))
root.geometry(f"600x600+{x}+{y}")


def open_task_form(task_number):
    task_form = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (600 / 2))
    y = int((screen_height / 2) - (700 / 2))
    task_form.geometry(f"600x600+{x}+{y}")
    task_form.title(f"Task {task_number} Form")

    if task_number == 1:
        X, Y = ReadSamplesFromFile(
            'E:/Studies/Level4-Semester1/Digital Signal Processing/Week 2/Lab 1/Signals/signal1.txt')
        PlotSamples(X, Y)
        task_instance = TaskOneForm(task_form, task_number)
    elif task_number == 2:
        X, Y = ReadSamplesFromFile(
            'E:/Studies/Level4-Semester1/Digital Signal Processing/Week 2/Lab 1/Signals/signal1.txt')
        task_instance = TaskTwoForm(task_form, task_number, X, Y)
    elif task_number == 3:
        task_instance = TaskThreeForm(task_form, task_number)
    elif task_number == 4:
        X, Y = ReadSamplesFromFile(
            'E:/Studies/Level4-Semester1/Digital Signal Processing/Week 2/Lab 1/Signals/signal1.txt')
        task_instance = TaskFourForm(task_form, task_number, X, Y)
    elif task_number == 5:
        task_instance = TaskSixForm(task_form, task_number)


tasks_frame = Frame(root)
tasks_frame.pack(padx=20, pady=20)

for i in range(1, 6):
    if i == 4:
        task_text = f"Task {i} - {i + 1}"
    elif i == 5:
        task_text = f"Task {i} - {i + 1} - {i + 2} - {i + 3} - {i + 4}"
    else:
        task_text = f"Task {i}"

    task_button = Button(tasks_frame, text=task_text, command=lambda num=i: open_task_form(num), width=30, height=4, bg='#34495e', fg='white')
    task_button.grid(row=i, column=0, pady=18)

root.mainloop()









