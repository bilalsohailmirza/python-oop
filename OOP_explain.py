
class Car:

    #this is the example of a prametarized constructor
    def __init__(self, make, model, engine, color, seating_capacity):
        self.make = make
        self.model = model
        self.engine = engine
        self.color = color
        self.seating_capcity = seating_capacity

    def Print1(self):
        print(self.make)
        print(self.model)
        print(self.engine)
        print(self.seating_capcity)     
        print(self.color)   


# if __name__ == '__main__':
car = Car('Toyota', 'Accord' ,'1500', 'Black', 5)
car1 = Car('Toyota', 'Corolla' ,'1500', 'Black', 5)
car2 = Car('Toyota', 'Prius' ,'1500', 'Black', 7)
car3 = Car('Honda', 'Civic' ,'1500', 'Black', 4)

print(getattr(car3, 'make'))
print(getattr(car3, 'model'))

car.print1()
car1.print1()
car2.print1()
car3.print1()


class Student:

    # def __init__(self): 
        #this is a construct that will construct our object
        # it initializes the values that our object is going to have
        # this is the example of a non-prametarized constructor
        # self.subjects = []
        # self.clubs = []
        # self.equipment = []
        # print('Hello From Constructor')

    def Print2(self):
        # self is used to locate the memory address of the object 
        # just like you locate a house with its address (house no.) 
        print()

student23 = Student()


# print(student1.subjects)



# CONSTRUCTORS 
# * Constructor is called automatically whenever a new instance of a class is  created
# * You can supply the arguments to the constructor when a new instance is created.
# * If you do not specify a constructor, the interpreter generates a default constructor for you







# 1. 1 -> 1 difference between procedural and OOP paradigm
# 2. Definition of class in detail
# 3. 4 Principles of OOP

