class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Skills:
    def __init__(self, language):
        self.language = language


class Programmer(Employee, Skills):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)       #it is use when we want parent constructor as well
        Skills.__init__(self, language)

p = Programmer("Prashant Kumar", 40000, "Python")

