# Functions
- Functions are a block of code that can be called by its name.
- Functions are used to avoid repetition of code.
- Functions are used to make code reusable.
- Functions are used to make code modular.
- Functions are used to make code readable.

## Syntax
```python
def function_name(parameters):
    # code to be executed
    return <expression>
```
- def is a keyword used to define a function.
- function_name is the name of the function.
- () is used to pass parameters to the function.

## How to call a function?
```python
def function_name():
    # code to be executed

function_name()
```


## Types
- Built-in functions
- User-defined functions

## Built-in functions
- Built-in functions are functions that are already defined in python.
- Built-in functions are available in python by default.

### Examples
- print()
- input()
- len()
- type()

## How to know if a function is built-in or user-defined?
- We can use the type() function to know if a function is built-in or user-defined.

```python
print(type(print)) # prints <class 'builtin_function_or_method'>
```

```python
def greet():
    print("Hello")

print(type(greet)) # prints <class 'function'>
```

## User-defined functions
- User-defined functions are functions that are defined by the user.
- User-defined functions are not available in python by default.
- User-defined functions are defined using the def keyword.

## Types of Functional Arguments

- Required arguments (positional arguments)
- Keyword arguments
- Default arguments
- Arbitrary arguments ( *args )
- Arbitrary keyword arguments ( **kwargs )

### Required arguments (positional arguments)

- Most common type of arguments.
- Values are passed to the function based on the position or order.
- The number of arguments passed to the function must match the number of parameters defined in the function.

### Example 1
```python
def greet(name):
    print("Hello", name)

greet("Ranjit") ✔️ #prints value
greet() ❌ #throws error
```

### Example 2
```python
def greet(name, age):
    print("Hello", name, "you are", age, "years old")

greet("Ranjit", 20) ✔️ #prints value
greet("Ranjit") ❌ #throws error
greet(20, "Ranjit") ❌ #throws error
```

In Python, we can use type hints to indicate the expected types of the parameters.

```python
def greet(name: str, age: int):
    print("Hello", name, "you are", age, "years old")

greet("Ranjit", 20) ✔️ #prints value
```
---
**Note:**
This is just a hint and not a constraint. We can still pass any type of value to the function.
---
To make it a constraint, we can use the assert keyword.

```python
def greet(name: str, age: int):
    assert type(name) == str, "name must be a string"
    assert type(age) == int, "age must be an integer"
    print("Hello", name, "you are", age, "years old")

greet("Ranjit", 20) ✔️ #prints value
```

#### Assignment
Write a function that takes two numbers as arguments and returns their sum.

```python
def perform_math_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Unsupported operator."

result_addition = perform_math_operation(5, 3, '+')
result_multiplication = perform_math_operation(4, 2, '*')
result_division = perform_math_operation(8, 2, '/')

```

    



### Keyword arguments

- Values are passed to the function based on the parameter name.
- Allows us to pass arguments in any order.
- The number of arguments passed must match the number of parameters defined in the function.
- This makes the code more readable.


### Example 1
```python
def person(name, age):
    print("Hello", name, "you are", age, "years old")

person(name="Ranjit", age=20) ✔️ #prints value

person(age=20, name="Ranjit") ✔️ #prints value

person("Ranjit", 20) ✔️ #prints value

person("Ranjit", age=20) ✔️ #prints value

person(name="Ranjit", 20) ❌ #throws error

person(age=20, "Ranjit") ❌ #throws error
```

#### Assignment
Write a function that takes two numbers as arguments and returns their sum.

```python
def perform_math_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Unsupported operator."

result_addition = perform_math_operation(num1=5, num2=3, operator='+')


