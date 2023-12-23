# `print()` function
- It is used to print the output to the screen.
- It can be used to print the output of any data type.
- Can be used to print multiple values at a time.
- We can use `sep` and `end` parameters to change the default behaviour of the `print()` function.

For Eg:

```python
# prints Hello World
print("Hello World")
```

```python
# prints 20
a = 20
print("The value of a is", a)
```

```python
# prints
# Ranjit
# Shrestha

first_name = "Ranjit"
last_name = "Shrestha"

print(first_name, last_name)
```

```python
# prints
# Ranjit Shrestha

first_name = "Ranjit"
last_name = "Shrestha"

print(first_name, end=" ")
print(last_name)
```

```python
# prints
# Ranjit Shrestha

first_name = "Ranjit"
last_name = "Shrestha"

print(first_name, last_name, sep=" ")
```

# Variables
- Variables are used to store data.
- Variables are the name attached to a value which can be changed & is used later in the code.
- No need to declare variables in Python.
value of the variable can be changed

For Eg:

```python
a = 20
```
here `a` is a label attached to the value `20`.

## Variable naming rules
- Variable names can only contain letters, numbers, and underscores. 
- Variable names can start with a letter or an underscore, but can not start with a number.
- Spaces are not allowed
- Variable names are case sensitive.
- Variable names should be short and descriptive, 
- Can not use python keywords as variable names. For eg: `print`, `if`, `else`, `for`, `while`, `True`, `False`, `None` etc.

For Eg:

```python
# valid variable names
a = 20
first_name = "Ranjit"
val1 = 20
_name = "Ranjit Shrestha"

```

```python
# invalid variable names
1a = 20
first name = 20
$abc = 20
```

## Variable naming conventions
- Use lowercase letters for variable names.
- Use underscores to separate words in a variable name.
- Though it is not mandatory to follow these conventions, it is a good practice to follow these conventions.

For Eg:

```python
first_name = "Ranjit"
last_name = "Shrestha"
age = 20
```

- For constant variables, use all uppercase letters.

 For eg:
 ```python
PI = 3.14
GRAVITY = 9.8
 ```


## Python vs C variable declaration

<table>
    <tr>
        <td><b>C Program</b></td>
        <td><b>Pyron</b></td>
    </tr>
    <tr>
        <td>int a = 20;</td>
        <td>a = 20</td>
    </tr>
    <tr>
        <td>float b = 20.5;</td>
        <td>b = 20.5</td>
    </tr>
    <tr>
        <td>char c = 'a';</td>
        <td>c = 'a'</td>
    </tr>
    <tr>
        <td>char str[] = "Hello World";</td>
        <td>str = "Hello World"</td>
    </tr>
    <tr>
        <td>In C, we need to declare the data type of the variable.</td>
        <td>In Python, we don't need to declare the data type of the variable.</td>
    </tr>
    <tr>
        <td>In C, we can not change the data type of the variable.</td>
        <td>In Python, we can change the data type of the variable.</td>
    </tr>
    <tr>
        <td>In C, variable refers to the memory location.</td>
        <td>In Python, variable refers to an object not the memory location.</td>
    </tr>
</table>

## Check the data type of the variable
- We can use `type()` function to check the data type of the variable.

For Eg:

```python
a = 20
print(type(a))
```

## Check the memory location of the variable
- We can use `id()` function to check the memory location of the variable.

For Eg:

```python
a = 20
print(id(a))
```

