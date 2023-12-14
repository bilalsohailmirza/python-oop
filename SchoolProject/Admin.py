import sqlite3

class Admin:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        data_tuple = (self.username, self.password)

        conn = sqlite3.connect('School.db')
        cursor = sqlite3.Cursor(conn)

        cursor.execute("""
                    INSERT 
                    INTO Admin 
                    VALUES (?,?)""", data_tuple
                    )
        
        conn.commit()
        conn.close()


    def login(self, username, password):
        pass



choice = int(input("Signup or Signin? \n 1. Sign Up\n2. Sign In\n\n"))

if choice == 1:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    admin = Admin(username, password)

elif choice == 2:
    pass
    # username = input('Enter your username: ')
    # password = input('Enter your password: ')
    # admin = Admin()
    # admin.login(username, password)
