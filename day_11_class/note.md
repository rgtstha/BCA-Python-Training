- Earlier programming languages are recognized as procedural languages. 
- Procedural languages are a set of instructions that tell the computer what to do step by step.
- Functional programming is a programming paradigm where programs are constructed by applying and composing functions.

## Problems with procedural programming
- Procedural programming is not very flexible.
- It is not easy to maintain.
- It is not easy to extend.
- It is not easy to reuse.
- It is not easy to test.

## Object Oriented Programming
- Object Oriented Programming is a programming paradigm where programs are constructed by objects.
- An object is a collection of data and methods that operate on its data.
- Objects are instances of classes.
- A class is a blueprint for creating objects.
- A class defines the properties and methods of an object.
- A class can be defined as a user-defined data type.
- A class can have data members and member functions.

## Classes
- A class is a user-defined data type.
- A class is the blueprint for creating objects.
- A class defines the properties and methods of an object.
- A class can have data members and member functions.

## Objects
- Real world entities are represented as objects.

### Class Syntax
```python
class ClassName:
    # class body

```

### Class naming convention
- Class names should start with a capital letter.
- Class names should not contain spaces.
- Class names should not start with a number.
- Class names should not contain special characters.

Example:
```python
class Person:
    name = "John" # member variable
    age = 36 # member variable
    country = "Norway" # member variable

    # member function or method
    def details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Country: ", self.country)

p1 = Person()
p1.details()

p1.name = "John Doe"
p1.age = 40

p1.details()
```

This is not very useful if we want to create multiple objects of the same class. We can use the `__init__()` method to initialize the object.

### The `__init__()` method

- The `__init__()` method is a special method that is called when an object is created.
- The `__init__()` method is also known as the constructor method.
- The `__init__()` method is used to initialize the object.
- The `__init__()` method is called automatically when an object is created.
- The `__init__()` method takes the `self` parameter which is a reference to the current instance of the class.
- The `__init__()` method can be used to initialize the object with values.

Example:
```python
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Country: ", self.country)

p1 = Person("John", 36, "Norway")

p1.details()
```

### The `self` parameter
- The `self` parameter is a reference to the current instance of the class.
- The `self` parameter is used to access the class variables and methods.



Real world example of using class insted of procedural programming:

Suppose we want a car with the properties like model, color, fuel type, etc. Also include a method start() to start the car.

### Procedural Programming
```python
model = "BMW"
color = "Black"
fuel_type = "Petrol"

def start():
    print(f"Starting the car {model} {color} {fuel_type}")

start()
```

This is not very useful if we want to create multiple cars. Because we have to create multiple variables for each car. Below is the example of creating multiple cars.

```python
model1 = "BMW"
color1 = "Black"
fuel_type1 = "Petrol"

model2 = "Audi"
color2 = "White"
fuel_type2 = "Diesel"

def start(model, color, fuel_type):
    print(f"Starting the car {model} {color} {fuel_type}")

start(model1, color1, fuel_type1)
start(model2, color2, fuel_type2)
```

This is not very useful if we want to create multiple cars. We can use the class to create multiple cars.

### Object Oriented Programming
```python
class Car:
    def __init__(self, model, color, fuel_type):
        self.model = model
        self.color = color
        self.fuel_type = fuel_type

    def start(self):
        print(f"Starting the car {self.model} {self.color} {self.fuel_type}")

car1 = Car("BMW", "Black", "Petrol")
car2 = Car("Audi", "White", "Diesel")

car1.start()
car2.start()
```

### Advantages:
- No need to create multiple variables for each car.


## Another example of class
Create a class called calculator with the following methods:
- add(x, y)
- subtract(x, y)
- multiply(x, y)
- divide(x, y)

```python
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x/self.y

    
    cal = Calculator(10, 5)
    print(cal.add())
    print(cal.subtract())
    print(cal.multiply())
    print(cal.divide())


```



