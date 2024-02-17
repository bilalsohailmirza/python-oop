
import MainModules, random, os

def quizMakerMainMenuModule():
        mainMenuOption = int(input("""/------======------======------\                              
|          Main  Menu          |
\------======------======------/
/------======------======------\ 
| - Create a Quiz          (1) |
| - Manage a Quiz          (2) |
| - Delete a Quiz          (3) |
| - Test a Quiz            (4) |
| - Exit                   (5) |
|                              |
|  __________________________  |
\------======------======------/\x1B[1F\r| """))
        print("\------======------======------/") 
        return mainMenuOption

def createAQuizGUI():
    print("""/------======------======------•------======------======------\                           
|                        Create A Quiz                        |
\------======------======------•------======------======------/
/------======------======------+------======------======------\                              
|    Question Configuration    |       Quiz Type Output       |
\------======------======------+------======------======------/                              
/------======------======------+------======------======------\ """)

def chooseQuestionLengthModule():
    createAQuizGUI()
    chooseQuestionLengthOption = int(input("""| Input Question Length:       |                              |
| - Input Value (From 3 To 15) |                              |
| - Random (Any Other Integer) |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
    print("\------======------======------+------======------======------/") 

    if chooseQuestionLengthOption >= 3 and chooseQuestionLengthOption <= 15:
        return chooseQuestionLengthOption
    
    elif chooseQuestionLengthOption == -1:
        chooseQuestionLengthOption = random.randint(3, 15)
        return chooseQuestionLengthOption
    
    else:
        MainModules.invalidInputModule()
        MainModules.loadingModule()
        return chooseQuestionLengthModule()

def chooseQuizTypeModule():
    createAQuizGUI()
    chooseQuizTypeOption = int(input("""| Choose Quiz Type:            |                              |       
| - User Input             (1) |                              |
| - Multiple Choice        (2) |                              |
|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
    print("\------======------======------+------======------======------/")

    if chooseQuizTypeOption == 1:
        chooseQuizTypeOption = "User Input Quiz     "
    
    elif chooseQuizTypeOption == 2:
        chooseQuizTypeOption = "Multiple Choice Quiz"
    
    else:
        MainModules.invalidInputModule()
        MainModules.loadingModule()
        return chooseQuizTypeModule()

    return chooseQuizTypeOption

def confirmQuizFeaturesModule(chooseQuestionLengthOption, chooseQuizTypeOption):
    createAQuizGUI()
    confirmQuizFeaturesOption = int(input("""| Take a look... -->           | Question Length: """+str(chooseQuestionLengthOption)+"""          
| Continue?                    | """+str(chooseQuizTypeOption)+"""         |
| - Yes, Continue          (1) |                              |
| - No, Return             (2) |                              |
|                              |                              |
|  __________________________  |                              |
\------======------======------+------======------======------/\x1B[1F\r| """))
    print("\------======------======------+------======------======------/")
    
    if confirmQuizFeaturesOption != 1 and confirmQuizFeaturesOption != 2:
        MainModules.invalidInputModule()
        MainModules.loadingModule()
        return confirmQuizFeaturesModule(chooseQuestionLengthOption, chooseQuizTypeOption)

    return confirmQuizFeaturesOption

def QuizConfiguartion():
    MainModules.loadingModule()
    mainMenuOption = quizMakerMainMenuModule()

    if mainMenuOption == 1:

        MainModules.loadingModule()
        chooseQuestionLengthOption = chooseQuestionLengthModule()
        MainModules.loadingModule()
        chooseQuizTypeOption = chooseQuizTypeModule()
        MainModules.loadingModule()
        confirmQuizFeaturesOption = confirmQuizFeaturesModule(chooseQuestionLengthOption, chooseQuizTypeOption)

        if confirmQuizFeaturesOption == 1:
            return chooseQuestionLengthOption, chooseQuizTypeOption
    
        elif confirmQuizFeaturesOption == 2:
            return QuizConfiguartion()

    else:
        print("! not finished !")
        MainModules.invalidInputModule()
        QuizConfiguartion()

# ↓↓↓ Code Below for Testing Purposes ↓↓↓ #

# chooseQuestionLengthOption, chooseQuizTypeOption = QuizConfiguartion()
# print(chooseQuestionLengthOption, chooseQuizTypeOption)
