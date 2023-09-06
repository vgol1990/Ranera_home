# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3


def CreateTable():
    con = sqlite3.connect('teatchers.db')
    cur = con.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS Students(
            Student_id INTEGER NOT NULL,
            Student_Name TEXT NOT NULL,
            School_id INTEGER NOT NULL PRIMARY KEY

        )"""

    sql = """
          CREATE TABLE IF NOT EXISTS School(
          School_id INTEGER NOT NULL,
          School_name TEXT NOT NULL
        )
    """
    cur.execute(sql)
    return


def close_connection(connection):
    if connection:
        connection.close()


def Insert_table():
    con = sqlite3.connect('teatchers.db')
    cur = con.cursor()

    sql = '''INSERT INTO Students
        VALUES 
            (? ,? ,?)'''
    arr = [
        (201, 'Иван', 1),
        (202, 'Петр', 2),
        (203, 'Анастасия', 3),
        (204, 'Игорь', 4)
    ]
    #cur.executemany(sql, arr)

    sql = '''INSERT INTO School
            VALUES  (?,?)'''
    arr = [
        ('1', 'Альтернатива'),
        ('2', 'Армат'),
        ('3', 'Новатор'),
        ('4', 'Эрудит')
    ]
    cur.executemany(sql, arr)

    con.commit()
    con.close()
    return


def Select_from_table():
    id = input('Введите id студента')
    con = sqlite3.connect('teatchers.db')
    cur = con.cursor()
    sql = 'SELECT * FROM Students'
    # sql = 'SELECT Student_Id, Student_Name, School_Id FROM Students WHERE Student_Id = ?", (id)'
    cur.execute(sql)
    arr = cur.fetchall()
    for i in range(len(arr)):
        print('id студента:', arr[1][0])
        print('Имя студента', arr[1][1])
        print('id школы:', arr[1][2])
        print('________________')



CreateTable()
Insert_table()
Select_from_table()