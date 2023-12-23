class Book:
    def __init__(self, title, author):
       # private properties
        self.__title = title
        self.__author = author
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            print(f"Book '{self.__title}' by {self.__author} has been borrowed.")
            self.__available = False
        else:
            print(f"Sorry, '{self.__title}' is currently not available.")

    def return_book(self):
        if not self.__available:
            print(f"Book '{self.__title}' has been returned.")
            self.__available = True
        else:
            print(f"This book is already in the library.")

    def __str__(self):
        status = "Available" if self.__available else "Not Available"
        return f"{self.__title} by {self.__author} - Status: {status}"




class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        title = book.get_title()
        if title not in self.books:
            self.books[title] = book
            print(f"Book '{title}' added to the library.")
        else:
            print(f"Book '{title}' is already in the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books.values():
                print(book)



library = Library()

while True:
        print("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. Display Books\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            new_book = Book(title, author)
            library.add_book(new_book)

        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            if title in library.books:
                library.books[title].borrow()
            else:
                print(f"Book '{title}' not found in the library.")

        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            if title in library.books:
                library.books[title].return_book()
            else:
                print(f"Book '{title}' not found in the library.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            print("Thankyou,see you again.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")