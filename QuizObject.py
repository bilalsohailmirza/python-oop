
import time, sqlite3, MainModules

class Quiz:

# note: for loop will be needed to determine whether or not quizid is taken
# if taken, do x += 1 until quiz id is free, put it back into query

    def quizTypeSegregatorModule(chooseQuestionLengthOption, chooseQuizTypeOption):
        MainModules.loadingModule()
        print(chooseQuestionLengthOption, chooseQuizTypeOption)
        if chooseQuizTypeOption == "User Input Quiz     ":
            MainModules.loadingModule()
            Quiz.userInputQuizModule(chooseQuestionLengthOption)
        else:
            print("okay great it works")

    def createAUserInputQuizGUI():
        print("""/------======------======------•------======------======------\                           
|                        Create A Quiz                        |
\------======------======------•------======------======------/
/------======------======------•------======------======------\                              
|                   Type In Questions Below                   |
\------======------======------•------======------======------/                              
/------======------======------•------======------======------\ """)

    def userInputQuizModule(chooseQuestionLengthOption):

# note: for loop will be needed based off of qu. length, make sure to link it to the sql query

        Quiz.createAUserInputQuizGUI()
        questionUserInput = input("""| Be Creative! (Maxiumum Character Length is 58)              |      

|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """)
        print("\------======------======------+------======------======------/")

        if len(questionUserInput) > 58:
            print("""/------======------======------\                              
|  Input exceeds 58 Character  |
|       Limit, Try Again       |
\------======------======------/""")
            
            Quiz.createAUserInputQuizGUI()
            return Quiz.userInputQuizModule(chooseQuestionLengthOption)

        # userPass = username, password
        # conn = sqlite3.connect('QuizGameDataBase.db')
        # cursor = sqlite3.Cursor(conn)
        # cursor.execute("""SELECT * FROM QuizCreation WHERE Username = ? AND Password = ?""", userPass,)
        # logInAttempt =  cursor.fetchone()

    def __init__(self):
        pass
    
QuizObject = Quiz()
