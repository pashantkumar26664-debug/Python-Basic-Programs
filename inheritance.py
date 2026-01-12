class Employee:                       # Parent Class
    company = 'Google'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(f'The name is {self.name} and the salary is {self.salary}')


class Programmer(Employee):           # Inherited Class
    company = 'Google Tech'

    def __init__(self, name, salary, language):
        super().__init__(name, salary)   # Call parent constructor
        self.language = language
        print(f'The language is {self.language}')


# Creating objects
a = Employee("Alice", 80000)
b = Programmer("Bob", 120000, "Python")

print(a.company, a.name, a.salary)
print(b.company, b.name, b.salary, b.language)
