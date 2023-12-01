

class Student:

    def __init__(self):

        self.subjects = []
        self.clubs = []

    def registerSubjects(self, subjects):
        self.subjects = subjects

    def joinClubs(self, clubs):
        self.clubs = clubs

    def getSubjects(self):
        return self.subjects
    




if __name__ == '__main__':

    student = Student()

    print("Do you want to enroll in any course?")
    print("Enter 1 to register or 2 to not")
    choice = int(input())
    if choice == 1:
        subject = input("Eneter the name of the subject")
        student.registerSubjects(subject)



# SQL

# DDL -> Data Definition Language
# DML -> Data Manipulation Language
# DCL -> Data Control Language 