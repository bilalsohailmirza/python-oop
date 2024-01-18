import sqlite3


class TimeTable:

    def __init__(self):
        self.table = [[]]
    # def viewTimeTable()

    def loadTimeTable(self):

        conn = sqlite3.connect('SchoolProjectDataBase.db')
        cursor = sqlite3.Cursor(conn)
        cursor.execute("""SELECT * FROM TimeTable""")

        rows = cursor.fetchall()
        return rows

    def viewTimeTable(self):
        rows = self.loadTimeTable()

        for i in range(len(rows)):
            rows[i] = list(rows[i])
            print(rows[i])

    def viewTimeTableByDays(self, day):
        conn = sqlite3.connect('SchoolProjectDataBase.db')
        cursor = sqlite3.Cursor(conn)
        day = day + '_'
        cursor.execute("""SELECT * FROM TimeTable WHERE Day LIKE ?""", (day,))
        
        rows = cursor.fetchall()
        return rows
    
    def viewTimeTableBySubject(self, subject):
        conn = sqlite3.connect('SchoolProjectDataBase.db')
        cursor = sqlite3.Cursor(conn)
        subject = subject + '%'
        cursor.execute("""SELECT * FROM TimeTable WHERE Subject LIKE ?""", (subject,))

        rows = cursor.fetchall()
        return rows


timetabletest = TimeTable()
timetabletest.loadTimeTable()
#timetabletest.viewTimeTable()

class Class:

    def __init__(self):
        self.subject = []
        self.instructor = []
        self.roomNo = []
        self.group = []

    def inputSubject(self, subject):
        self.subject = subject
    def inputInstructor(self, instructor):
        self.instructor = instructor
    def inputRoomNo(self, roomNo):
        self.roomNo = roomNo
    def inputGroup(self, group):
        self.group = group

    def getClassAttr(self):
        return self.subject, self.instructor, self.roomNo, self.group

    def displayClass(self):
        print("Subject:    ",self.subject)
        print("Instructor: ",self.instructor)
        print("Room No:    ",self.roomNo)
        print("Group:      ",self.group)

# example2 = Class()

# subject = input("Enter your subject: ")
# example2.inputSubject(subject.capitalize())
# instructor = input("Enter your teacher: ")
# example2.inputInstructor(instructor.upper())
# roomNo = input("Enter your room number: ")
# example2.inputRoomNo(roomNo.upper())
# group = input("Enter your group: ")
# example2.inputGroup(group.upper())

# example2.displayClass()