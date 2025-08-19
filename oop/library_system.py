# library_system.py

# Base class
class Book:
    def init(self, title: str, author: str):
        self.title = title
        self.author = author

    def str(self):
        return f"Book: {self.title} by {self.author}"


# Derived class EBook
class EBook(Book):
    def init(self, title: str, author: str, file_size: int):
        super().init(title, author)  # Call base class constructor
        self.file_size = file_size

    def str(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class PrintBook
class PrintBook(Book):
    def init(self, title: str, author: str, page_count: int):
        super().init(title, author)  # Call base class constructor
        self.page_count = page_count

    def str(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition: Library class
class Library:
    def init(self):
        self.books = []  # Stores Book, EBook, and PrintBook instances

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)