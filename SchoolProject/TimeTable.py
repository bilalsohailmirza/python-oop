import sqlite3

class TimeTable:

    def __init__(self):
        self.table = []


    def loadTimeTable(self):
        
        conn = sqlite3.connect('School3.db')
        cursor = sqlite3.Cursor(conn)

        cursor.execute("""
                    SELECT *
                    FROM TimeTable
                    """
                    )
        
        rows = cursor.fetchall()
        return rows
        
                
    def viewTimeTableByDays(self, day):
         
        conn = sqlite3.connect('School3.db')
        cursor = sqlite3.Cursor(conn)
        day = day + '_'
        cursor.execute("""SELECT * FROM TimeTable WHERE Day LIKE ?;""", (day,))
        
        rows = cursor.fetchall()

        return rows

    def viewTimeTable(self):

        rows = self.loadTimeTable()

        for i in range(len(rows)):
            rows[i] = list(rows[i])
            print(rows[i])

class Class:

    def __init__(self, subject, instructor, room_no, group_no):

        self.subject = subject
        self.instructor = instructor
        self.room_no = room_no
        self.group_no = group_no

    def display_class(self):
        print("Subject:  ", self.subject)
        print("Instructor:  ", self.instructor)
        print("Room No:  ", self.room_no)
        print("Group No:  ", self.group_no)



if __name__ == '__main__':

    time_table = TimeTable()
    # time_table.loadTimeTable()
    # time_table.viewTimeTable()
    
