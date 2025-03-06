import sqlite3

connection = sqlite3.connect('fash.db')
cursor = connection.cursor()
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS teacher (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    fio TEXT
);
    
    
    '''
)
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS class (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT
);


    '''
)
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    lastname TEXT,
    patronymic TEXT, 
    class_id INTEGER,
    FOREIGN KEY(class_id) REFERENCES class(id)
);


    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    FOREIGN KEY(teacher_id) REFERENCES teacher(id)
);


    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS timetable (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    subject_id INTEGER,
    teacher_id  INTEGER,
    class_id INTEGER,
    weekday TEXT,
    lesson_order INTEGER,
    start_time TEXT,
    end_time TEXT,
    classroom TEXT,
    homework TEXT,
    FOREIGN KEY(teacher_id) REFERENCES teacher(id),
    FOREIGN KEY(class_id) REFERENCES class(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
);


    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS grade (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    grade_value TEXT,
    grade_type TEXT,
    grade_comment TEXT,
    topic TEXT,
    subject_id INTEGER,
    teacher_id  INTEGER,
    student_id  INTEGER,
    datetime TIMESTAMP,
    FOREIGN KEY(teacher_id) REFERENCES teacher(id),
    FOREIGN KEY(student_id) REFERENCES student(id)
);


    '''
)