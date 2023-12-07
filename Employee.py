class Employee:

    def __init__(self, firstName, lastName, monthlySalary):

        self.firstName = firstName
        self.lastName = lastName
        if(monthlySalary < 0):
            self.monthlySalary = 0.0
        else:
            self.monthlySalary = monthlySalary

    def getYearlySalary(self):
        return self.monthlySalary * 12
    
    def getYearlyRaise(self, yearlyRaise, yearlySalary):
        raisedSalary =  yearlyRaise * yearlySalary
        return raisedSalary
        
Employee1 = Employee('Justin', 'Nowak', 4500)
Employee2 = Employee('Bilal', 'Mirza', 3200)

Employee1YearlySalary = Employee1.getYearlySalary
Employee2YearlySalary = Employee2.getYearlySalary

print("Yearly Salary of employee 1 is: ",Employee1YearlySalary())
print("Yearly Salary of employee 2 is: ",Employee2YearlySalary())

yearlyRaise = 1.1
Employee1RaisedSalary = Employee1.getYearlyRaise(yearlyRaise, Employee1YearlySalary)
Employee2RaisedSalary = Employee1.getYearlyRaise(yearlyRaise, Employee2YearlySalary)

print()
print("Yearly Salary of employee 1 after raise is: ",Employee1RaisedSalary())
print("Yearly Salary of employee 2 after raise is: ",Employee2RaisedSalary())