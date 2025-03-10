import tkinter as tk
from tkinter import *

# def show_timetable():
#     for i, row



root = Tk()
root.title('ds')
root.geometry('1012x512')
root.configure(bg='gray')
subjects_frame = tk.Frame(root,bg='gray')
timetable = []
if not timetable:
    subject_frame = tk.Frame(root, bg='gray')
    no_subjects_label = tk.Label(subject_frame, text='Ура! Сегодня нет уроков!',font=('Arial', 21), bg='gray', )












    subject_frame.pack()
    no_subjects_label.pack()
root.mainloop()