class Person:
    def __init__(self, name, age, add, sal):
        self.name = name
        self.age = age
        self.add = add

class Employee:
    def __init__(self,emp_id, sal):
        self.emp_id = emp_id
        self.sal = sal 

    def display(self):
        print(f"Name={self.name}\n Age = {self.age}\n Address= {self.add}\n Salary= {self.sal}")
        
class Developer(Employee, Person):
    def __init__(self, name, age, add, sal, programming_lang):
        Person.__init__(name, age, add)
        Employee.__init__(1,  sal)
        self.programming_lang = programming_lang

    def display(self):
        super().display()
        print(f"Language= {self.programming_lang}")

dev1 = Developer(
    "Anuj",
    23,
    "Kathmandu",
    25000,
    "Python"
)

dev1.display()