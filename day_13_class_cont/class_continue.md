# Magic/Dunder Methods
- Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
- Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading.
- Few examples for magic methods are: __init__, __add__, __len__,  etc.

## Example of Magic Methods
```python
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def __str__(self):
        return f" Name: {self.name}\n Id: {self.id}\n Salary: {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __ge__(self, other):
        return self.salary >= other.salary


emp1 = Employee("Emp1", 1, 10000)
emp2 = Employee("Emp2", 2, 20000)

print(emp1)
print(emp2)

print(emp1 + emp2)

print(len(emp1))
print(len(emp2))

print(emp1 == emp2) # emp1.__eq__(emp2)
print(emp1 < emp2) # emp1.__lt__(emp2)
print(emp1 > emp2) # emp1.__gt__(emp2)
print(emp1 <= emp2) # emp1.__le__(emp2)
print(emp1 >= emp2) # emp1.__ge__(emp2)
```


# Inheritance
- It is a way to form new classes using classes that have already been defined.
- The newly formed classes are called derived classes, the classes that we derive from are called base classes.

## Why do we need inheritance?
- It provides reusability of a code.
- We don’t have to write the same code again and again. 
- Also, it allows us to add more features to a class without modifying it.

#### Real World scenario where inheritance can be applied
- Consider we are make employee management system for a IT company. In the company, there are many types of employees like developers, testers, managers etc. All these employees have some common behavior like all of them have name, id, salary and they also do get paid, sleep, eat etc. So, we can make a base class Employee which will have all these common behaviors. Then we can make different classes for different type of employees like Developer, Tester, Manager etc. These classes will inherit the common behavior from the base class Employee. So, we can say that the Developer, Tester, Manager etc. classes are derived from the base class Employee. Each of these classes will have its own unique behavior. For example, Developer will have a behavior of writing code, Tester will have a behavior of testing the code etc. So, we can say that the Developer, Tester, Manager etc. classes are derived from the base class Employee.

## How to implement inheritance in Python?
- In Python, inheritance can be implemented by using the following syntax:
```python
class BaseClass:
    # Body of base class

class DerivedClass(BaseClass):
    # Body of derived class
```

- Here, the derived class inherits the base class.

## Example of Inheritance in Python
```python
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print(f" Name: {self.name}\n Id: {self.id}\n Salary: {self.salary}")

class Developer(Employee):
    # developer may have some unique attributes like, programming language, 
    def __init__(self, name, id, salary, language):
        super().__init__(name, id, salary)
        self.language = language

    def display(self): # overriding
        # super().display()
        print(f" Language: {self.language}")

class Designer(Employee):
    # designer may have some unique attributes like, designing tool, 
    def __init__(self, name, id, salary, tool):
        super().__init__(name, id, salary)
        self.tool = tool

    def display(self):
        super().display()
        print(f" Tool: {self.tool}")


dev1 = Developer("Dev1", 1, 10000, "Python")
dev2 = Developer("Dev2", 2, 20000, "Java")

des1 = Designer("Des1", 3, 30000, "Adobe XD")
des2 = Designer("Des2", 4, 40000, "Figma")

dev1.display()
dev2.display()

des1.display()
des2.display()
```
