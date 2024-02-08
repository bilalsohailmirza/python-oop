from TimeTable import TimeTable
from utils import displayDayChoices, displaySubjectChoice
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

    def displayTimeTableBySubject(self, subject):
        timetabletest = TimeTable()
        tableRows = timetabletest.viewTimeTableBySubject(subject)

        for rows in tableRows:
            print(rows)

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
        day_choice = displayDayChoices()

        if day_choice == 1:
            student.displayTimeTableByDays('Mon')
        elif day_choice == 2:
            student.displayTimeTableByDays('Tue')
        elif day_choice == 3:
            student.displayTimeTableByDays('Wed')
        elif day_choice == 4:
            student.displayTimeTableByDays('Thu')
        elif day_choice == 5:
            student.displayTimeTableByDays('Fri')

    elif option == 3:
        subjectChoice = displaySubjectChoice()
        
        if subjectChoice == 1:
            student.displayTimeTableBySubject('Eng')
        elif subjectChoice == 2:
            student.displayTimeTableBySubject('Mat')
        elif subjectChoice == 3:
            student.displayTimeTableBySubject('Che')
        elif subjectChoice == 4:
            student.displayTimeTableBySubject('Phy')
        elif subjectChoice == 5:
            student.displayTimeTableBySubject('Bio')
        elif subjectChoice == 6:
            student.displayTimeTableBySubject('Rel')
        elif subjectChoice == 7:
            student.displayTimeTableBySubject('Phy')
        elif subjectChoice == 8:
            student.displayTimeTableBySubject('I A')
        elif subjectChoice == 9:
            student.displayTimeTableBySubject('Ger')
        elif subjectChoice == 10:
            student.displayTimeTableBySubject('Com')
        elif subjectChoice == 11:
            student.displayTimeTableBySubject('Bus')
        elif subjectChoice == 12:
            student.displayTimeTableBySubject('Art')
