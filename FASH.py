import tkinter as tk
import sqlite3
from tkinter import messagebox, ttk
from datetime import date
from datetime import timedelta
import os




def main_app():
    loading_label.pack_forget()
    choice_label.pack()
    register_button.pack()
    auth_button.pack()


def connect_db():
    return sqlite3.connect("users.db")


# Создание таблицы пользователей, если она не существует
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        phone TEXT UNIQUE,
        password TEXT,
        gender TEXT,
        role TEXT)''')
    conn.commit()
    conn.close()


create_table()


def open_registration_window():
    reg_window = tk.Toplevel(root)
    reg_window.geometry('912x512')
    reg_window.title('ФЭШ,регистрация')
    reg_window.configure(bg='gray')
    PR_Label = tk.Label(reg_window, text='!Предупреждение: после регистрации вам нужно будет войти в созданный вами аккаунт!', font=('Arial', 15), bg='gray')
    DAN_label = tk.Label(reg_window, text='Пожалуйста, введите свои данные:', font=('Arial', 21), bg='gray')
    FIO_label = tk.Label(reg_window, text='ФИО:', font=('Arial', 21), bg='gray')
    FIO_entry = tk.Entry(reg_window, width=30)
    DAN_label.grid(row=0, column=0)
    FIO_label.grid(row=1, column=0)
    FIO_entry.grid(row=1, column=1)

    NOM_label = tk.Label(reg_window, text='Номер телефона:', font=('Arial', 21), bg='gray')
    NOM_entry = tk.Entry(reg_window, width=30)
    NOM_label.grid(row=2, column=0)
    NOM_entry.grid(row=2, column=1)

    PASS_label = tk.Label(reg_window, text='Пароль (от 8 символов):', font=('Arial', 21), bg='gray')
    PASS_entry = tk.Entry(reg_window, width=30)
    PASS_label.grid(row=3, column=0)
    PASS_entry.grid(row=3, column=1)

    POL_label = tk.Label(reg_window, text='Пол:', font=('Arial', 21), bg='gray')
    pol = tk.StringVar()

    POL_Button = tk.Radiobutton(reg_window, variable=pol, value='Мужской', text='Мужской')
    POL_Button2 = tk.Radiobutton(reg_window, variable=pol, value='Женский', text='Женский')
    POL_label.grid(row=4, column=0)
    POL_Button.grid(row=4, column=1)
    POL_Button2.grid(row=4, column=2)

    rol = tk.StringVar()

    ROL_Button = tk.Radiobutton(reg_window, variable=rol, value='Ученик', text='Ученик')
    ROL_Button2 = tk.Radiobutton(reg_window, variable=rol, value='Учитель', text='Учитель')
    ROL_label = tk.Label(reg_window, text='Роль в ФЭШ:', font=('Arial', 21), bg='gray')
    ROL_label.grid(row=5, column=0)
    ROL_Button.grid(row=5, column=1)
    ROL_Button2.grid(row=5, column=2)

    def register():
        fio = FIO_entry.get()
        nom = NOM_entry.get()
        pas = PASS_entry.get()
        pol_v = pol.get()
        rol_v = rol.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users(fullname,phone,password,gender,role) VALUES(?,?,?,?,?)',
                       (fio, nom, pas, pol_v, rol_v))
        messagebox.showinfo('Вы успешно зарегистрированы!', 'Нажмите на <<OK>> и войдите в свой созданный аккаунт!', )
        reg_window.destroy()
        # messagebox.showerror('Ошибка!', 'Неверный номер телефона или пароль!')
        conn.commit()
    POLZ_Button = tk.Button(reg_window, text='Cтать пользователем ФЭШ', font=('Arial', 21), bg='gray', command=register)
    POLZ_Button.grid(row=7, column=0)
def get_monday(curdate):
    return curdate - timedelta(days=curdate.weekday())
def define_month():
    pass
    global current_monday, days_frame
    monday_month = current_monday.month
    sunday=current_monday+timedelta(days=6)
    print(current_monday, sunday)
    sunday_month = sunday.month
    print(monday_month)
    print(sunday_month)
    if monday_month == sunday_month:
        month_Label.configure(text=current_monday.strftime('%B %Y'), font=('Arial', 18))
    else:
        f_month = current_monday.strftime('%B')
        s_month = sunday.strftime('%B')
        year1 = current_monday.strftime('%Y')
        year2 = sunday.strftime('%Y')
        text = f'{f_month} - {s_month} {year1}'
        month_Label.configure(text=text)


def update_week(delta=0):
    global current_monday, buttons, month_Label
    current_monday += timedelta(weeks=delta)
    define_month()
    for i in range(7):
        day = current_monday + timedelta(days=i)
        buttons[i].config(text=day.day)
def open_PACPICANIE_window():
    pass
def open_OCENKI_widnow():
    pass
def open_D3_window():
    pass
def open_PROFIL_window():
    pass
def open_KLACC_window():
    pass

def open_PACPICANIE_teacher_window():
    pass
def open_HYPNALI_teacher_window():
    pass
def open_KLACCI_teacher_window():
    pass

def open_student_window():
    global current_monday, buttons, month_Label, days_frame
    frame.pack_forget()
    root.title('Дневник ФЭШ')
    student_frame=tk.Frame(root, bg='gray')
    PACPICANIE_Button = tk.Button(student_frame, text='Расписание', font=('Arial', 18), bg='gray', command=open_PACPICANIE_window)
    OCENKN_Button = tk.Button(student_frame, text='Оценки', font=('Arial', 18), bg='gray')
    D3_Button = tk.Button(student_frame, text='Домашние Задания', font=('Arial', 18), bg='gray')
    PROFIL_Button = tk.Button(student_frame, text='Профиль', font=('Arial', 18), bg='gray')
    KLACC_Button = tk.Button(student_frame, text='Класс', font=('Arial', 18), bg='gray')
    # days_frame=tk.Frame(root, bg='gray')
    prev_button = tk.Button(days_frame, text ='←', font=('Arial', 12), command=lambda:update_week(-1))
    next_button = tk.Button(days_frame, text ='→', font=('Arial', 12), command=lambda: update_week(1))


    days=['Пн','Вт','Ср','Чт','Пт','Сб','Вс']

    current_monday = get_monday(date.today())
    define_month()
    month_Label = tk.Label(days_frame, bg='gray',text=current_monday.strftime('%B %Y'), font=('Arial', 18))
    month_Label.grid(row=0, column=+1, columnspan=7)
    buttons = []
    for i,day in enumerate(['Пн','Вт','Ср','Чт','Пт','Сб','Вс']):
        button = tk.Button(days_frame, text = '', width=4)
        button.grid(row=1,column=i+1)
        buttons.append(button)
        tk.Label(days_frame,text=day, bg = 'gray', font=('Arial', 18)).grid(row=2,column=i+1)
    print(current_monday)
    PACPICANIE_Button.grid(row=0, column=0)
    OCENKN_Button.grid(row=0, column=1)
    D3_Button.grid(row=0, column=2)
    PROFIL_Button.grid(row=0, column=3)
    KLACC_Button.grid(row=0, column=4)
    prev_button.grid(row=1,column=0)
    next_button.grid(row=1,column=8)
    student_frame.pack()
    days_frame.pack()
    update_week()


def open_teaher_window():
    global current_monday, buttons, month_Label, days_frame
    frame.pack_forget()
    root.title('ФЭШ')
    teacher_frame=tk.Frame(root, bg='gray')
    FASH_V_Label = tk.Label(teacher_frame, text='ФЭШ', font=('Arial', 21), bg='gray')
    Teacher_Label = tk.Label(teacher_frame, text='Учитель', font=('Arial', 21), bg='Cyan', compound="center")
    prev_button = tk.Button(days_frame, text='←', font=('Arial', 12), command=lambda: update_week(-1))
    next_button = tk.Button(days_frame, text='→', font=('Arial', 12), command=lambda: update_week(1))

    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

    current_monday = get_monday(date.today())
    define_month()
    month_Label = tk.Label(days_frame, bg='gray', text=current_monday.strftime('%B %Y'), font=('Arial', 18))
    month_Label.grid(row=0, column=+1, columnspan=7)
    buttons = []
    for i, day in enumerate(['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']):
        button = tk.Button(days_frame, text='', width=4)
        button.grid(row=1, column=i + 1)
        buttons.append(button)
        tk.Label(days_frame, text=day, bg='gray', font=('Arial', 18)).grid(row=2, column=i + 1)
    print(current_monday)
    FASH_V_Label.grid(row=0, column=0)
    Teacher_Label.grid(row=0, column=1)
    teacher_frame.pack(anchor='nw')
    prev_button.grid(row=1,column=0)
    next_button.grid(row=1,column=8)
    days_frame.pack()
    update_week()

def open_login_window():
    login_window = tk.Toplevel(root)
    login_window.geometry('912x512')
    login_window.title('ФЭШ, вход в аккаунт')
    login_window.configure(bg='gray')
    bxod_Label = tk.Label(login_window, text='Вход:', font=('Arial', 21), bg='gray')
    NOM2_Label = tk.Label(login_window, text='Номер телефона:', font=('Arial', 21), bg='gray')
    NOM2_Entry = tk.Entry(login_window, width=30)
    PAROL_Label = tk.Label(login_window, text='Пароль:', font=('Arial', 21), bg='gray')
    PAROL_Entry = tk.Entry(login_window, width=30)
    bxod_Label.grid(row=0, column=0)
    NOM2_Label.grid(row=1, column=0)
    NOM2_Entry.grid(row=1, column=1)
    PAROL_Label.grid(row=2, column=0)
    PAROL_Entry.grid(row=2, column=1)

    def login():
        phone_number = NOM2_Entry.get()
        password = PAROL_Entry.get()
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE phone=? and password=?', (phone_number, password))
        user=cursor.fetchone()
        print(user)
        if user is not None:
            messagebox.showinfo('Вы успешно авторизованы!', 'Нажмите на <<OK>> и вы попадёте в ФЭШ!', )
            login_window.destroy()
            if user[5]== 'Ученик':
                open_student_window()
            else:
                open_teaher_window()
        else:
            messagebox.showerror('Ошибка!', 'Неверный номер телефона или пароль!')
    BXOD_Button = tk.Button(login_window, text='Войти в аккаунт', font=('Arial', 21), bg='gray', command=login)
    BXOD_Button.grid(row=7, column=0)

root = tk.Tk()
root.title('Фейковая Электронная Школа')
root.geometry('1012x612')
root.configure(bg='gray')





# Регистрация или вход
frame= tk.Frame(root, bg='gray')

greeting_label = tk.Label(frame, text='ФЭШ приветствует вас!', font=('Arial', 21), bg='gray')
greeting_label.pack()
loading_label = tk.Label(frame, text='Подождите! Идёт загрузка...', font=('Arial', 21), bg='gray')
loading_label.pack(pady=180)
choice_label = tk.Label(frame, text='Пожалуйста, зарегистрируйтесь или войдите в свой аккаунт!', font=('Arial', 21),
                        bg='gray')

register_button = tk.Button(frame, text='Регистрация', font=('Arial', 21), bg='gray', fg='black',
                            command=open_registration_window)

auth_button = tk.Button(frame, text='Вход', font=('Arial', 21), bg='gray', fg='black', command=open_login_window)

root.after(2000, main_app)
current_monday = date.today()
buttons = []
month_Label = tk.Label(bg='gray',text=current_monday.strftime('%B %Y'), font=('Arial', 18))
days_frame = tk.Frame(root, bg='gray')
frame.pack()
root.mainloop()
