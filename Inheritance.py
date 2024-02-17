# SIMPLE INHERITANCE EXAMPLE

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def person_print(self):
#         print("Print from person")

# class Employee(Person):

#     def __init__(self, name, age, emp_id, salary):
        
#         super().__init__(name, age)

#         self.emp_id = emp_id
#         self.salary = salary


# person = Person("Bilal", 22)
# employee = Employee("Justin", 15, 23, 4500)

# person.person_print()
# employee.person_print()
# print(employee.name)


# MULTIPLE INHERITANCE EXAMPLE

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_print(self):
        print("Print from person")
        
class Musician(Person):
    
    def __init_(self, name, age, genre, band):

        Person.__init__(self, name, age)
        self.genre = genre
        self.band = band

class Artist(Person):

    def __init__(self, name, age, pieces_made, style):

        Person.__init__(name, age)
        self.pieces_made = pieces_made
        self.style = style

class Athelete(Person):

    def __init__(self, name, age, level):

        Person.__init__(name, age)
        self.level = level

   
class Guitarist(Musician):

    def __init__(self, name, age, genre, band, type_of_guitar, performances_played):
        # Person.__init__(self, name, age)
        Musician.__init__(self, name, age, genre, band)

        self.type_of_guitar = type_of_guitar
        self.performances_played = performances_played

    # def __repr__(self) -> str:
    #     return f"Name: {self.name}, Age: {self.age} Genre: {self.genre} Band: {self.band}"

    # __function_name__ -> Magic / Dunder Methods
class Painter(Artist):

    def __init__(self, name, age, pieces_made, style, era):
        super().__init__(name, age, pieces_made, style)

        self.era = era


class Sprinter(Athelete):

    def __init__(self, name, age, level, race_types, top_speed):
        super().__init__(name, age, level)

        self.race_types = race_types
        self.top_speed = top_speed


chris_martin = Guitarist("Chris Martin", 45, "Rock", "Coldplay", "Acoustic", 152)
print(chris_martin)
