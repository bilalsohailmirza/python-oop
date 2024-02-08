
def displayDayChoices():
    day_choice = int(input("""Enter the day you want the time table for?\n
1. Monday\n
2. Tuesday\n
3. Wednesday\n
4. Thursday\n
5. Friday\n
"""))
    
    return day_choice

def displaySubjectChoice():
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
    
    return subjectChoice

def displayUpdateChoices():

    print("""Enter the Day and Subject you want to update:
(Day1/2)
(Subject)                    
""")
    dayUpdateChoice = input()
    subjectUpdateChoice = input()

    updateInfo = [""]*4

    updateInfo[0] = input("Enter new Subject: ")
    updateInfo[1] = input("Enter new Teacher: ")
    updateInfo[2] = input("Enter new RoomNo: ")
    updateInfo[3] = input("Enter new GroupNo: ")

    return dayUpdateChoice, subjectUpdateChoice, updateInfo

def displayInsertOptions():
    print("Enter the details of the class: ")

    insertInfo = [""]*6

    insertInfo[0] = input("Enter the Day: ")
    insertInfo[1] = input("Enter new Subject: ")
    insertInfo[2] = input("Enter new Teacher: ")
    insertInfo[3] = input("Enter new RoomNo: ")
    insertInfo[4] = input("Enter new GroupNo: ")
    insertInfo[5] = int(input("Enter the Period: "))

    return insertInfo
    
def displayDeleteOptions():

    day = input("Enter the Day: ")
    subject = input("Enter the Subject: ")

    return day, subject

fflush(stdin)

# info = displayInsertOptions()
# print(info)