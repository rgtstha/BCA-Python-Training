
# Why do we need data types?
1. For efficient use of memory.
2. To help maintain the integrity of the data. Insures that operations are performed on data in a meaningful way and prevent unexpected behavior or errors.
3. Type checking allows a compiler to check the logic of the program before the program is actually run. For eg: `a = 10 + "Hello"` will give an error because we can not add integer and string.
4. 

## Data Types in Python
1. **Numeric Data Types** -  (int, float, complex)
2. **Sequence Data Types** - (str, list, tuple, range)
3. **Boolean Data Type** - (bool)
4. **Set Data Type** - (set, frozenset)
5. **Mapping Data Type** - (dict)
6. **Binary Data Type** - (bytes, bytearray, memoryview) # we will not cover this in this lecture
7. **None Data Type** - (None)


## Numeric Data Types
In numeric data types, we can perform mathematical operations like addition, subtraction, multiplication, division, etc.
1. **int** - Integers are whole numbers, positive or negative, without decimals.

    ```python
    a = 10 
    a = int(10)
    b = -10
    c = 0
    print(type(a)) # <class 'int'>
    print(a+b) # 0
    print(a-b) # 20
    print(a*b) # -100
    print(a/b) # -1.0

    ```
2. **float** - Floats are real numbers, with a decimal point dividing the integer and fractional parts.

    ```python
    a = 10.5
    b = -10.5
    c = 0.0

    n1 = float(10)
    print(n1) # 10.0
    print(type(n1)) # <class 'float'>
    print(a+b) # 0.0
    ```

3. **complex** - Complex numbers are written with a "j" as the imaginary part.

    ```python
    a = 10 + 5j
    b = -10 + 5j
    c = 0 + 5j

    n1= complex(10, 5)
    print(n1) # 10 + 5j
    print(type(n1)) # <class 'complex'>
    print(a+b) # 0 + 10j
    print(a.real) # 10.0
    print(a.imag) # 5.0

    ```

<!-- table -->
<table width="100%">
    <tr>
        <td><b>Int</b></td>
        <td><b>Float</b></td>
        <td><b>Complex</b></td>
    </tr>
    <tr>
        <td>10</td>
        <td>10.5</td>
        <td>10 + 5j</td>
    </tr>
    <tr>
        <td>-10</td>
        <td>-10.5</td>
        <td>-10 + 5j</td>
    </tr>
    <tr>
        <td>0</td>
        <td>0.0</td>
        <td>0 + 5j</td>
    </tr>
    <tr>
        <td>int(10)</td>
        <td>float(10)</td>
        <td>complex(10, 5)</td>
    </tr>

</table>


## Sequence Data Types
In sequence data types, we can perform operations like indexing, slicing, concatenation, repetition, etc.
1. **str** - Strings are used to store text data. Strings are immutable.

    ```python
    a = "Hello World"
    b = 'Hello World'
    c = """Hello World"""
    d = '''Hello World'''
    e = str("Hello World")
    
    print(type(a)) # <class 'str'>
    print(a[0]) # H
    print(a[0:5]) # Hello
    print(a[0:5:2]) # Hlo
    print(a[::-1]) # dlroW olleH

    print(a[-4:-1]) # orl
    print(a[-4:]) # orld
    print(a[:-1]) # Hello Worl

    print(a[2:]) # llo World
    ```

    ### Slice Notation
    - it returns a new slice object.
    - used in sequence data types like str, list and tuple
    - positive value in `step` means forward direction and negative value in `step` means backward direction.
    
        Syntax:
        ```python
        slice(start, stop, step)

        # or
        a[start:stop:step]
        ```

        <table>
        <tr>
        <td><b>start</b></td>
        <td><b>Optional. An integer number specifying at which position to start the slicing. Default is 0</b></td>
        </tr>
        <tr>
        <td><b>stop</b></td>
        <td><b>An integer number specifying at which position to end the slicing</b></td>
        </tr>
        <tr>
        <td><b>step</b></td>
        <td><b>Optional. An integer number specifying the step of the slicing. Default is 1</b></td>
        </tr>
        </table>

