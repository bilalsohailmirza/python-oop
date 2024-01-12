from TimeTable import TimeTable
import sqlite3
from os import system
import time

class Student:

    def signup_student(self, username, password):

        data_tuple = (username, password)

        conn = sqlite3.connect('School.db')
        cursor = sqlite3.Cursor(conn)

        cursor.execute("""
                    INSERT 
                    INTO Student 
                    VALUES (?,?)""", data_tuple
                    )
        
        conn.commit()
        conn.close()


    def login_student(self, username, password):

        conn = sqlite3.connect('School3.db')
        cursor = sqlite3.Cursor(conn)

        cursor.execute("""
                    SELECT *
                    FROM Student 
                    WHERE username = ? AND password = ?""", (username, password)
                    )
        
        result = cursor.fetchone()
        # print(result)
        
        if result:
            print("You have been logged in!", result[0])
            time.sleep(2)
            system('clear')
            return username
        else:
            pass

        conn.commit()
        conn.close()

    def displayTimeTableByDays(self, day):
        
        time_table = TimeTable()
        table_rows = time_table.viewTimeTableByDays(day)

        for row in table_rows:
            print(row)


    def displayTimeTable(self):

        time_table = TimeTable()
        time_table.viewTimeTable()

# if __name__ == '__main__':

# student = Student()

choice = int(input("Signup or Signin? \n1. Sign Up\n2. Sign In\n\n"))

if choice == 1:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    student = Student()
    student.signup_student(username, password)

elif choice == 2:
    
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    student = Student()
    student_name = student.login_student(username, password)

    print("Welcome ", student_name)
    option = int(input("""1. View TimeTable\n
                        2. View TimeTable by Days\n
                        3. View TimeTable by Subject\n 
                       """))

    if option == 1:
        student.displayTimeTable()

    elif option == 2:
        day_choice = int(input("""Enter the day you want the time table for?
                           1. Monday
                           2. Tuesday
                           """))

        if day_choice == 1:
            student.displayTimeTableByDays('Mon')