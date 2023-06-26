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

# import sqlite3

#создение таблицы

# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY);"""
# cursor.execute(query)
# connection.commit()
# connection.close()

# import sqlite3

# # Наполнение таблицы
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Student_Id , Student_Name , School_Id)
# VALUES
# ('201', 'Иван', 1),
# ('202', 'Петр', 2),
# ('203', 'Анастасия', 3),
# ('204', 'Игорь', 4);"""
# cursor.execute(query)
# connection.commit()
# connection.close()



import sqlite3

# Информация о школе и студенте
def get_connection():
    connection = sqlite3.connect('teachers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()
        
def get_school_name(school_id):
     try:
          connection = get_connection()
          cursor = connection.cursor()
          query = "SELECT * FROM School WHERE School_Id = ?"
          cursor.execute(query,(school_id,))
          record = cursor.fetchone()
          close_connection(connection)
          return record[1]
     except (Exception, sqlite3.Error) as error:
           print ('Ошибка в получении данных ', error)
#get_school_name(1)

def get_student(student_id):
    try:
      connection = get_connection()
      cursor = connection.cursor()
      query = """SELECT * FROM Students WHERE School_Id = ?"""
      cursor.execute(query,(student_id,))
      records = cursor.fetchall()
	  #school_name = get_school_name(row[2]) 
     #print (records)
      #print ("Информацияо школе и студенте:")
      for row in records:
          print ("ID студента:", row[0])
          print ("Имя студента:", row[1])
          print ("ID школы:", row[2])
          print ("Название школы:", get_school_name(row[2]), "\n")
      close_connection(connection)
    except (Exception, sqlite3.Error) as error:
      print ('Ошибка в получении данных ', error)

get_student(1)
get_student(2)
get_student(3)   
get_student(4)