import sqlite3

class TimeTable:

    def __init__(self):
        self.table = [[]]


    def loadTimeTable(self):

        for i in range(5):
            for j in range(5):

                print(self.table[])
                # result = whatever you read from database
                table[2][3] = result 
        
    def viewTimeTable():

        for i in range(5):
            for j in range(5):

                print(self.table[])

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

    class1 = Class('Chemistry', 'MC', 'A5', '10S1')
    class1.display_class()
