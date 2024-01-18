from TimeTable import TimeTable
import sqlite3, os, time

class Student:

    def signup(self, username, password):

        dataTuple = (username, password)
        conn = sqlite3.connect('SchoolProjectDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO Student VALUES (?, ?)""", dataTuple)

        conn.commit()
        conn.close()

    def login(self, username, password):

        conn = sqlite3.connect('SchoolProjectDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT * FROM Student WHERE Username = ? AND Password = ?""", (username, password))

        result = cursor.fetchone()
        if result:
            print("You have been logged in!", result[0])
            time.sleep(2)
            os.system('cls')
            return username
        else:
            print('Wrong Credentials!! Try Again..')
            Student.login()

        conn.commit()
        conn.close()
    
    def displayTimeTable(self):
        timetabletest = TimeTable()
        timetabletest.viewTimeTable()

    def displayTimeTableByDays(self, day):
        timetabletest = TimeTable()
        tableRows = timetabletest.viewTimeTableByDays(day)

        for rows in tableRows:
            print(rows)

    def displayTimeTableBySubject(self, subject):
        timetabletest = TimeTable()
        tableRows = timetabletest.viewTimeTableBySubject(subject)

        for rows in tableRows:
            print(rows)

choice = int(input("Signup or Signin? \n1. Sign Up\n2. Sign In\n\n"))

if choice == 1:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    student = Student()
    student.signup(username, password)
elif choice == 2:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    student = Student()
    studentName = student.login(username, password)

    print("Welcome, ",studentName)
    option = int(input("""\n1. View TimeTable
2. View TimeTable by Days
3. View TimeTable by Subject
"""))
    if option == 1:
        student.displayTimeTable()
    elif option == 2:
        dayChoice = int(input("""Enter the day you want the time table for?\n
1. Monday
2. Tuesday
3. Wednesday
4. Thrusday
5. Friday
"""))
        if dayChoice == 1:
            student.displayTimeTableByDays('Mon')
        elif dayChoice == 2:
            student.displayTimeTableByDays('Tue')
        elif dayChoice == 3:
            student.displayTimeTableByDays('Wed')
        elif dayChoice == 4:
            student.displayTimeTableByDays('Thu')
        elif dayChoice == 5:
            student.displayTimeTableByDays('Fri')

    elif option == 3:
        subjectChoice = int(input("""Enter the subject you want the time table for?\n

1. English
2. Mathematics
3. Chemistry
4. Physics
5. Biology
6. Religious Education
7. Physical Education
8. I AM
9. German
10. Comupter Science
11. Business
12. Art and Design

"""))
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

#student = Student()
