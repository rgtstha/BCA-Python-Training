class Book:
    def __init__(self, title: str, author:str, ISBN:str):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __str__(self) -> str:
        return f"Title:{self.title}, Author: {self.author}, ISBN: {self.ISBN} "