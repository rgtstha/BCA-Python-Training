# Access Modifiers
- determines the visibility and accessibility of a class's properties and methods
- In Python, there are three types of access modifiers:
    - public
    - protected
    - private

- In python, access modifiers are not strictly enforced  

## Why do we need access modifiers?
- To protect the data from accidental manipulation
- To achieve data encapsulation

## Public Access Modifier
- By default, all the properties and methods are public
- We can access public properties and methods from anywhere in the program

Example:
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

## Protected Access Modifier
- We can declare a property or method as protected by adding a single underscore before the name of the property or method
- Can be accessed only within the class and its subclasses
- To declare a member as protected, we need to add a single underscore before the name of the member (_)

Example:
```python
class Car:
    def __init__(self, model, color, fuel_type):
        self.model = model
        self.color = color
        self._fuel_type = fuel_type

    def start(self):
        print(f"Starting the car {self.model}{self.color} {self._fuel_type}")

car1 = Car("BMW", "Black", "Petrol")

print(car1._fuel_type)
```

### When to use protected access modifier?

- When we want to prevent the data from being modified accidentally
- When we want to prevent the data from being accessed from outside the class



## Private Access Modifier
- We can declare a property or method as private by adding a double underscore before the name of the property or method (__)
- Can be accessed only within the class

Example:
```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

# Usage
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)

```

# Getters and Setters
Getters and setters are used to access or modify the private attributes of a class.

## Getters
- Getters are used to access the private attributes of a class
- Getters are also called accessor methods

Real world example:
```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount(5000)
account.deposit(1000)
account.withdraw(2000)

print(account.get_balance())
```

## Setters
- Setters are used to modify the private attributes of a class
- Setters are also called mutator methods

Real world example:
```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  #

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

