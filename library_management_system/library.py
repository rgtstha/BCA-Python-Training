from book import Book
from student import Student

class Library:
    def __init__(self) -> None:
        self.books = []
        self.students = []


    def add_book(self, book: Book):
        self.books.append(book)

    def add_student(self, student: Student):
        self.students.append(student)