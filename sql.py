import json
import sqlite3
from datetime import  datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk

# def show_timetable():
#     for i, row

# Подключаемся к базе данных
conn = sqlite3.connect('fash.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE Student 
ADD COLUMN role TEXT
""")
conn.commit()
#
# # Создание таблицы Class (Класс)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Class (
#     class_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL
# )
# ''')
#
# # Создание таблицы Teacher (Преподаватель)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Teacher (
#     teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL
# )
# ''')
#
# cursor.execute('''
# INSERT INTO Teacher(name)
# VALUES('Полякова Ольга Станиславовна')
#
# ''')
# conn.commit()
# cursor.execute('''
# ALTER TABLE Grade
#  ADD COLUMN view TEXT''')
# conn.commit()
#
#
# # Создание таблицы Subject (Предмет)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Subject (
#     subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     teacher_id INTEGER,
#     FOREIGN KEY (teacher_id) REFERENCES Teacher (teacher_id)
# )
# ''')
#
# cursor.execute('''
# INSERT INTO Subject(name,teacher_id)
# VALUES('Програмированние', 1)
#
# ''')
# conn.commit()
# # Создание таблицы Student (Ученик)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Student (
#     student_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     class_id INTEGER,
#     FOREIGN KEY (class_id) REFERENCES Class (class_id)
# )
# ''')
#
# # Создание таблицы Timetable (Расписание)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Timetable (
#     timetable_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     class_id INTEGER,
#     weekday TEXT NOT NULL,
#     lesson_order INTEGER NOT NULL,
#     lesson_type TEXT NOT NULL,
#     start_time TEXT,
#     end_time TEXT,
#     subject_id INTEGER,
#     classroom TEXT,
#     homework TEXT,
#     FOREIGN KEY (class_id) REFERENCES Class (class_id),
#     FOREIGN KEY (subject_id) REFERENCES Subject (subject_id)
# )
# ''')
#
#
#
#
# # Таблица Topic (Темы уроков)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Topic (
#     topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     subject_id INTEGER,
#     topic_name TEXT NOT NULL,
#     FOREIGN KEY (subject_id) REFERENCES Subject (subject_id)
# )
# ''')
 # Таблица Grade (Оценки)
 # cursor.execute('''
 # CREATE TABLE IF NOT EXISTS Grade (
 #     grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
 #     student_id INTEGER,
 #     topic_id INTEGER,
 #       subject_id INTEGER,
 #     lesson_date TEXT,       -- Дата проведения урока для хронологической сортировки
 #     grade_type TEXT,        -- Тип оценки (например, контрольная, оценка с комментарием, "Н" – пропуск и т.д.)
 #     grade_value TEXT,       -- Значение оценки (числовое, буквенное и т.п.)
 #     comment TEXT,           -- Комментарий к оценке (если есть)
 #    FOREIGN KEY (student_id) REFERENCES Student (student_id),
 #    FOREIGN KEY (topic_id) REFERENCES Topic (topic_id)
 # )
 # '''
 #            )

#
# topics = [
#     # Для Математики (subject_id = 1)
#     (1, "Алгебра и геометрия"),
#     # Для Русского языка (subject_id = 2)
#     (2, "Орфография и пунктуация"),
#     # Для Окружающего мира (subject_id = 3)
#     (3, "Погода и климат"),
#     (4, "Растения и животные")
# ]
#
# cursor.executemany(
#     "INSERT INTO Topic (subject_id, topic_name) VALUES (?, ?)",
#     topics
# )
# conn.commit()

# grades = [
#     # Для ученика с student_id = 1 по предмету Окружающий мир (например, тема "Погода и климат", topic_id = 3)
#     (1, 3, "2025-02-01", "Контрольная", "5", "Отлично"),
#     (1, 3, "2025-02-05", "Ответ", "4", "Хорошо"),
#     # Для того же ученика по теме "Растения и животные" (topic_id = 4)
#     (1, 4, "2025-02-10", "Домашняя работа", "3", "Интересное наблюдение"),
#     # Пример пропуска урока (тип оценки "Пропуск", значение "Н")
#     (1, 3, "2025-02-15", "Пропуск", "Н", "Не явился"),
#     # Для другого ученика (student_id = 2) по предмету Русский язык (тема "Орфография и пунктуация", topic_id = 2)
#     (2, 2, "2025-02-03", "Контрольная", "4", "Удовлетворительно")
# ]
#
# cursor.executemany("""
# INSERT INTO Grade (student_id, topic_id, lesson_date, grade_type, grade_value, comment)
# VALUES (?, ?, ?, ?, ?, ?)
# """, grades)
#
# conn.commit()

# students = [('Иванов Иван Иванович', 1), ('Петров Петр Петрович', 2), ('Сидоров Сидор Сидорович', 3),
#             ('Кузнецова Мария Александровна', 4), ('Михайлова Екатерина Сергеевна', 5),
#             ('Федоров Алексей Владимирович', 6), ('Егорова Наталья Ивановна', 7),
#             ('Шмидт Павел Константинович', 8), ('Гусева Алла Николаевна', 9), ('Смирнова Ольга Викторовна', 10)]
# cursor.executemany('INSERT INTO Student (name, class_id) VALUES (?, ?)', students)
# conn.commit()

# timetable = [
#     (1, 'Пн', 1, 'lesson', '08:00', '08:40', 1, '301', 'Домашка 1'),
#     (1, 'Вт', 2, 'lesson', '09:00', '09:40', 2, '302', 'Домашка 2'),
#     (2, 'Ср', 1, 'lesson', '08:00', '08:40', 3, '303', 'Домашка 3'),
#     (2, 'Чт', 2, 'lesson', '09:00', '09:40', 4, '304', 'Домашка 4'),
#     (3, 'Пн', 1, 'lesson', '08:00', '08:40', 5, '305', 'Домашка 5'),
#     (3, 'Вт', 2, 'lesson', '09:00', '09:40', 6, '306', 'Домашка 6'),
#     (4, 'Ср', 1, 'lesson', '08:00', '08:40', 7, '307', 'Домашка 7'),
#     (4, 'Чт', 2, 'lesson', '09:00', '09:40', 8, '308', 'Домашка 8'),
#     (5, 'Пн', 1, 'lesson', '08:00', '08:40', 9, '309', 'Домашка 9'),
#     (5, 'Вт', 2, 'lesson', '09:00', '09:40', 10, '310', 'Домашка 10')
# ]
# cursor.executemany('''
# INSERT INTO Timetable (class_id, weekday, lesson_order, lesson_type, start_time, end_time, subject_id, classroom, homework)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
# ''', timetable)
# conn.commit()

# Пример заполнения таблицы Class данными
# classes = [('5A',), ('5B',), ('6A',), ('6B',), ('7A',), ('7B',), ('8A',), ('8B',), ('9A',), ('9B',)]
# cursor.executemany('INSERT INTO Class (name) VALUES (?)', classes)
#
# # Пример заполнения таблицы Teacher данными
# teachers = [('Иванов Иван Иванович',), ('Тотфалушина Ксения Викторовна',), ('Сидоров Сидор Сидорович',),
#             ('Смирнова Ольга Викторовна',), ('Кузнецова Мария Александровна',),
#             ('Михайлова Екатерина Сергеевна',), ('Федоров Алексей Владимирович',),
#             ('Егорова Наталья Ивановна',), ('Шмидт Павел Константинович',), ('Гусева Алла Николаевна',)]
# cursor.executemany('INSERT INTO Teacher (name) VALUES (?)', teachers)
# conn.commit()
student_id = 1
current_date = datetime.today().strftime('%Y-%m-%d')
weekday = 'Пн'


SQL_QUERY = """
WITH TodaySchedule AS (
    SELECT t.class_id, t.weekday, t.lesson_order, t.start_time, t.end_time,
           t.subject_id, t.classroom, t.homework
    FROM Timetable t
    WHERE t.class_id = (SELECT class_id FROM Student WHERE student_id = ?)
      AND t.weekday = ?
   )
SELECT ts.lesson_order, ts.start_time || '-' || ts.end_time AS lesson_time,
       ts.classroom, sub.name AS subject_name, ts.homework,
       (SELECT json_group_array(json_object('value', g.grade_value, 'type', g.grade_type, 'view', g.view))
        FROM Grade g
        JOIN Topic top ON g.topic_id = top.topic_id
        WHERE g.student_id = ? AND top.subject_id = ts.subject_id) AS grades
FROM TodaySchedule ts
JOIN Subject sub ON ts.subject_id = sub.subject_id
GROUP BY ts.lesson_order
ORDER BY ts.lesson_order;
"""
# cursor.execute(SQL_QUERY)

cursor.execute(SQL_QUERY, (student_id, weekday, student_id))
timetable = cursor.fetchall()
conn.close()

def get_image_path(type,value):
    if type == 'оценка' and value == '5':
        return 'оценка5.png'
    if type == 'оценка' and value == '4':
        return 'оценка4.png'
    if type == 'оценка' and value == '3':
        return 'оценка3.png'
    if type == 'оценка' and value == '2':
        return 'оценка2.png'

    if type == 'оценкаКР' and value == '5':
        return 'оценка5КР.png'
    if type == 'оценкаКР' and value == '4':
        return 'оценка4КР.png'
    if type == 'оценкаКР' and value == '3':
        return 'оценка3КР.png'
    if type == 'оценкаКР' and value == '2':
        return 'оценка2КР.png'

    if type == 'оценкаКОММ' and value == '5':
        return 'оценка5ком.png'
    if type == 'оценкаКОММ' and value == '4':
        return 'оценка4ком.png'
    if type == 'оценкаКОММ' and value == '3':
        return 'оценка3ком.png'
    if type == 'оценкаКОММ' and value == '2':
        return 'оценка2ком.png'

    if type == 'оценкаКРКОММ' and value == '5':
        return 'оценка5КР.ком.png'
    if type == 'оценкаКРКОММ' and value == '4':
        return 'оценка4КР.ком.png'
    if type == 'оценкаКРКОММ' and value == '3':
        return 'оценка3КР.ком.png'
    if type == 'оценкаКРКОММ' and value == '2':
        return 'оценка2КР.ком.png'

    if type == 'оценкаможниспр' and value == '4':
        return 'оценка4.можниспр.png'
    if type == 'оценкаможниспр' and value == '3':
        return 'оценка3.можниспр.png'
    if type == 'оценкаможниспр' and value == '2':
        return 'оценка2.можниспр.png'


def display_schedule():
    global subjects_frame
    for i,row in enumerate(timetable):
        lesson_frame = ttk.Frame(subjects_frame,relief="groove",borderwidth=2, padding=5)
        text_frame = ttk.Frame(lesson_frame)
        text_frame.pack(side=tk.LEFT)
        title=f'{row[0]} урок  {row[1]} , кабинет {row[2]}'
        title_label = tk.Label(text_frame,text=title)
        subname_label = tk.Label(text_frame, text=row[3])
        d3_label = tk.Label(text_frame, text=row[4])
        title_label.pack()
        subname_label.pack()
        d3_label.pack()
        lesson_frame.pack()
        grades = json.loads(row['grades']) if row['grades'] else []
        grades_frame = tk.Frame(lesson_frame,bg='gray80')
        grade = grades[0]
        print('Формат', grade)
        # for grade in grades:
        #     grade_label = tk.Label(grades_frame, text=)
        image_path = get_image_path(grade['view'],grade['value'])
        print(image_path)
        foto= tk.PhotoImage(file=image_path)
        foto = foto.subsample(5, 5)
        grade_label = tk.Button(grades_frame, image=foto)
        grade_label.photo = foto

        grades_frame.pack(side=tk.RIGHT, padx=20 )
        grade_label.pack()

root = Tk()
root.title('ds')
root.geometry('1012x512')
root.configure(bg='gray')
subjects_frame = tk.Frame(root,bg='gray')
subjects_frame.pack()
if not timetable:
    subject_frame = tk.Frame(root)
    no_subjects_label = tk.Label(subject_frame, text='Ура! Сегодня нет уроков!',font=('Arial', 21), bg='gray', )
    subject_frame.pack()
    no_subjects_label.pack()

else:
    display_schedule()



print(timetable)



root.mainloop()