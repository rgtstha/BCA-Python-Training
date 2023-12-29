
# Modules in Python

- Modules are files containing Python code.

- Modules can be imported into other modules or into the main module.

- Modules are used to organize code into logical units.

- Modules are imported using the `import` keyword.

## Creating a module

Let's first write normal python code.
```python

class Book:
    self __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"{self.title} by {self.author}")

    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display_info()


book1 = Book("Introduction to Programming"," Ram ")
book2 =  Book("Introduction to Python"," Shyam ")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.display_books()

```

here, when the program gets bigger, it will be difficult to manage the code. So, we can create a module for each class.

Let's create a module for the `Book` class.

```python
# book.py

class Book:
    self __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"{self.title} by {self.author}")
```

Now, we can import the `Book` class from the `book` module.

```python
import book
```

Now, we can use the `Book` class from the `book` module.

```python
book1 = book.Book("Introduction to Programming"," Ram ")

book1.display_info()
```

Instead of using book.Book, we can use alias name for the module.

```python
import book as bk

book1 = bk.Book("Introduction to Programming"," Ram ")

book1.display_info()
```

We can also import the `Book` class directly from the `book` module.

```python
from book import Book

book1 = Book("Introduction to Programming"," Ram ")

book1.display_info()
```

We can also import all the classes from the `book` module.

```python
from book import *

book1 = Book("Introduction to Programming"," Ram ")

book1.display_info()
```



