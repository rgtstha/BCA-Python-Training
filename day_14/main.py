from book import Book
from library import Library

book_1 = Book("Introduction to Computer", "Charles")

library = Library()
library.add_book(book_1)

library.count_books()