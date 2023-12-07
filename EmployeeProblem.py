
class Employee:

    def __init__(self, firstName, lastName, monthlySalary):

        self.firstName = firstName
        self.lastName = lastName

        if(monthlySalary < 0):
            self.monthlySalary = 0.0
        else:
            self.monthlySalary = monthlySalary

    def get_yearly_salary(self):

        return self.monthlySalary * 12

    def give_yearly_raise(self, yearlyRaise, yearlySalary)

        raisedSalary = yearlySalary * 12 * yearlyRaise
        return raisedSalary



if __name__ == '__main__':

    emp1 = Employee('Justin', 'Waller', 4500)
    emp2 = Employee('Bilal', 'Javed', 3200)
    
    emp1_yearly_salary = emp1.get_yearly_salary()
    emp2_yearly_salary = emp2.get_yearly_salary()

    print("Yearly Salary of Employee1 is: ", emp1_yearly_salary)
    print("Yearly Salary of Employee2 is: ", emp2_yearly_salary)

    yearly_raise = 1.1

    emp1_raised_salary = emp1.give_yearly_raise(yearly_raise, emp1_yearly_salary)
    emp2_raised_salary = emp2.give_yearly_raise(yearly_raise, emp2_yearly_salary)

    print('\n\n')
    print("Yearly Salary of Employee 1 after raise: ", emp1_raised_salary)
    print("Yearly Salary of Employee 2 after raise: ", emp2_raised_salary)













