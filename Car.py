from typing import Any


class Car:

    #this is the example of a prametarized constructor
    def __init__(self, make, model, engine, color, seating_capacity):
        self.make = make
        self.model = model
        self.engine = engine
        self.color = color
        self.seating_capcity = seating_capacity

    def printData(self):
        print(self.make)
        print(self.model)
        print(self.engine)
        print(self.seating_capcity)     
        print(self.color)

   # there are 2 types of functions to modify data
   # 1. Accessors -> Access and return the data (get functions)
   # 2. Mutators -> Mutate/Update the data (set Functions)

    def getMake(self):
        # print(self.make)
        return self.make
    
    def setMake(self, newMake):
        self.make = newMake

    def getModel(self):
        return self.model
    
    def setModel(self, newModel):
        self.model = newModel
        

car = Car('Honda' ,'Accord', 1500, 'Black', 5)

print(car.getModel())

car.setModel('Civic')

print(car.getModel())
