from TimeTable import TimeTable
from utils import *
import sqlite3
from os import system
import time

class Admin:

    def signup_admin(self, username, password):

        data_tuple = (username, password)

        conn = sqlite3.connect('School3.db')
        cursor = sqlite3.Cursor(conn)

        cursor.execute("""
                    INSERT 
                    INTO Admin 
                    VALUES (?,?)""", data_tuple
                    )
        
        conn.commit()
        conn.close()

    def my_print(self):
        print("Hello from my_print()\n")


    def login(self, username, password):

        conn = sqlite3.connect('School3.db')
        cursor = sqlite3.Cursor(conn)

        cursor.execute("""
                    SELECT *
                    FROM Admin 
                    WHERE Username = ? AND Password = ?""", (username, password)
                    )
        
        result = cursor.fetchone()
        # print(result)
        
        if result:
            print("You have been logged in!", result[0])
            self.my_print()
            return username
        else:
            pass

        conn.commit()
        conn.close()

    def displayTimeTable(self):
        timetable = TimeTable()
        timetable.viewTimeTable()

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

    def updateSubject(self, day, subject, updateInfo):

        conn = sqlite3.connect('School3.db')
        cursor = sqlite3.Cursor(conn)
        
        cursor.execute("""UPDATE TimeTable SET Subject=?, Teacher=?, RoomNo=?, GroupNo=? WHERE
ROWID=69""", (updateInfo[0], updateInfo[1], updateInfo[2], updateInfo[3]))
        
        conn.commit()
        conn.close()

    def insertClass(self, insertInfo):

        conn = sqlite3.connect('School3.db')
        cursor = sqlite3.Cursor(conn)
        
        cursor.execute("""INSERT INTO TimeTable VALUES(?, ?, ?, ?, ?, ?)""", (insertInfo[0], insertInfo[1], insertInfo[2], insertInfo[3], insertInfo[4], insertInfo[5]))
        
        conn.commit()
        conn.close()

    def deleteClass(self, day, subject):

        conn = sqlite3.connect('School3.db')
        cursor = sqlite3.Cursor(conn)
        
        cursor.execute("""DELETE FROM TimeTable  WHERE Day = ? AND Subject = ?""", (day, subject))
        
        conn.commit()
        conn.close()

choice = int(input("Signup or Signin? \n 1. Sign Up\n2. Sign In\n\n"))

if choice == 1:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    admin = Admin()
    admin.signup_admin(username, password)

elif choice == 2:
    
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    admin = Admin()
    admin.login(username, password)

    choice = int(input("""Enter the operation you want to perform?
                       
    1. View Time Table
    2. Update Time Table
    3. Add a new record to Time Table
    4. Delete a Record from Time Table 
"""))

    if choice == 1:
        viewingOption = int(input("""Choose your viewing format: 

    1. View Complete Time Table
    2. View Time Table by Days
    3. View Time Table by Subjects
                                   
"""))
        if viewingOption == 1:
            admin.displayTimeTable()

        elif viewingOption == 2:
            day_choice = displayDayChoices()

            if day_choice == 1:
                admin.displayTimeTableByDays('Mon')
            elif day_choice == 2:
                admin.displayTimeTableByDays('Tue')
            elif day_choice == 3:
                admin.displayTimeTableByDays('Wed')
            elif day_choice == 4:
                admin.displayTimeTableByDays('Thu')
            elif day_choice == 5:
                admin.displayTimeTableByDays('Fri')

        elif viewingOption == 3:
            subjectChoice = displaySubjectChoice()


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

        dayUpdateChoice, subjectUpdateChoice, insertInfo = displayUpdateChoices()
        admin.updateSubject(dayUpdateChoice, subjectUpdateChoice, insertInfo)
    
    elif choice == 3:
        insertInfo = displayInsertOptions()
        admin.insertClass(insertInfo)

    elif choice == 4:
        day, subject = displayDeleteOptions()
        admin.deleteClass(day, subject)
#Admin Roles: ``
    # Viewing Time Table by Days [x]
    # Viewing TImeTable by Subject [x]
    # Update the Existing Schedule UPDATE [x]
    # Insert New entries in the Time Table []
    # Delete the existing entries in the time table []
    # CRUD 
    # C -> Create
    # R -> Read
    # U -> Updade
    # D -> Delete