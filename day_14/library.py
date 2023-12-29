from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def count_books(self):
        print(f"Total books:{len(self.books)}")
