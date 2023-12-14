import sqlite3

class Admin:

    def __init__(self):
        pass

    def signup_admin(self, username, password):

        data_tuple = (username, password)

        conn = sqlite3.connect('School.db')
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

        conn = sqlite3.connect('School.db')
        cursor = sqlite3.Cursor(conn)

        cursor.execute("""
                    SELECT *
                    FROM Admin 
                    WHERE Name = ? AND Password = ?""", (username, password)
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
