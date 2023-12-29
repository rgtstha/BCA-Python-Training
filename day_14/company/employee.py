class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print(f" Name: {self.name}\n Id: {self.id}\n Salary: {self.salary}")
