# Polymorphism
- Poly means many and morphism means forms. So polymorphism means many forms.

In programming, polymorphism refers to methods/functions/operators having the same name but different implementations.

Example of polymorphic functions:
`len()` function is a polymorphic function because it can be used to find the length of a string, list, tuple, dictionary etc.

```python
print(len("Hello"))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({"name": "John", "age": 36}))
```

Example of polymorphic operators:
`+` operator is a polymorphic operator because it can be used to add two integers or two floats or two strings.

```python
print(10 + 20)

print(10.5 + 20.5)

print("Hello" + "World")
```

Polymorphism in OOP:
- Polymorphism is often used in class method, where a method having the same name is defined in multiple classes.

Example:
```python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):

    animal.sound()  

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

Another real world example:
```python

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


square = Square(5)
rectangle = Rectangle(5, 10)

print(square.area())
print(rectangle.area())
```

Real World Example Assignment:
```python
# Base class
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def calculate_salary(self):
        return "Base salary calculation"

# Subclass 1: Manager
class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name, role="Manager")
        self.team_size = team_size

    def calculate_salary(self):
        base_salary = 50000
        team_bonus = self.team_size * 1000
        return base_salary + team_bonus

# Subclass 2: Developer
class Developer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name, role="Developer")
        self.programming_language = programming_language

    def calculate_salary(self):
        base_salary = 60000
        language_bonus = 2000 if self.programming_language == "Python" else 0
        return base_salary + language_bonus

# Function that calculates salary for any employee
def calculate_employee_salary(employee):
    return employee.calculate_salary()

# Create instances of Manager and Developer
manager = Manager(name="Alice", team_size=5)
developer = Developer(name="Bob", programming_language="Python")

# Use the calculate_employee_salary function with different employees
print(calculate_employee_salary(manager))    # Output: Manager's salary calculation with team bonus
print(calculate_employee_salary(developer))  # Output: Developer's salary calculation with language bonus

```