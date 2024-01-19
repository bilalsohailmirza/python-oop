from TimeTable import TimeTable
from Utilities import displayDayChoices, displaySubjectChoices
import sqlite3, os, time

class Admin:

    def signup(self, username, password):

        dataTuple = (username, password)
        conn = sqlite3.connect('SchoolProjectDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""INSERT INTO Admin VALUES (?, ?)""", dataTuple)

        conn.commit()
        conn.close()

    def login(self, username, password):

        conn = sqlite3.connect('SchoolProjectDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT * FROM Admin WHERE Username = ? AND Password = ?""", (username, password))

        result = cursor.fetchone()
        if result:
            print("You have been logged in!", result[0])
            return username
        else:
            print('Wrong Credentials!! Try Again..')
            Admin.login()

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
        timetable = TimeTable()
        tableRows = timetable.viewTimeTableBySubject(subject)

        for rows in tableRows:
            print(rows)

choice = int(input("Signup or Signin? \n1. Sign Up\n2. Sign In\n\n"))

if choice == 1:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    admin = Admin()
    admin.signup(username, password)
elif choice == 2:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    admin = Admin()
    admin.login(username, password)

    choice = int(input("""Enter the operation you want to perform:
 
1. View TimeTable
2. Update TimeTable
3. Add to Timetable          
"""))
    if choice == 1:
        viewingOption = int(input("""Choose your viewing format:
 
1. View Complete TimeTable
2. View TimeTable by Days
3. View TimeTable by Subject      
"""))
        if viewingOption == 1:
            admin.displayTimeTable()

        elif viewingOption == 2:
            dayChoice = displayDayChoices()

            if dayChoice == 1:
                admin.displayTimeTableByDays('Mon')
            elif dayChoice == 2:
                admin.displayTimeTableByDays('Tue')
            elif dayChoice == 3:
                admin.displayTimeTableByDays('Wed')
            elif dayChoice == 4:
                admin.displayTimeTableByDays('Thu')
            elif dayChoice == 5:
                admin.displayTimeTableByDays('Fri')

        elif viewingOption == 3:
            subjectChoice = displaySubjectChoices()
        
        if subjectChoice == 1:
            admin.displayTimeTableBySubject('Eng')
        elif subjectChoice == 2:
            admin.displayTimeTableBySubject('Mat')
        elif subjectChoice == 3:
            admin.displayTimeTableBySubject('Che')
        elif subjectChoice == 4:
            admin.displayTimeTableBySubject('Phy')
        elif subjectChoice == 5:
            admin.displayTimeTableBySubject('Bio')
        elif subjectChoice == 6:
            admin.displayTimeTableBySubject('Rel')
        elif subjectChoice == 7:
            admin.displayTimeTableBySubject('Phy')
        elif subjectChoice == 8:
            admin.displayTimeTableBySubject('I A')
        elif subjectChoice == 9:
            admin.displayTimeTableBySubject('Ger')
        elif subjectChoice == 10:
            admin.displayTimeTableBySubject('Com')
        elif subjectChoice == 11:
            admin.displayTimeTableBySubject('Bus')
        elif subjectChoice == 12:
            admin.displayTimeTableBySubject('Art')

    elif choice == 2:
        pass
    elif choice == 3:
        pass
