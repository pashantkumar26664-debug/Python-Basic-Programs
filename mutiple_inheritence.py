class Employee:                           #Parent class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_employee(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


class Skills:                             #Parent class
    def __init__(self, language):
        self.language = language

    def show_skills(self):
        print(f"Programming Language: {self.language}")


class Programmer(Employee, Skills):   # Multiple Inheritance                          
    def __init__(self, name, salary, language):
        Employee.__init__(self, name, salary)
        Skills.__init__(self, language)

    def show_programmer(self):
        print("---- Programmer Details ----")
        self.show_employee()
        self.show_skills()


# Creating object
p = Programmer("Alice", 120000, "Python")

p.show_programmer()
