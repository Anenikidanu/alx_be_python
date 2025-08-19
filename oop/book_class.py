# book_class.py

class Book:
    def init(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def del(self):
        print(f"Deleting {self.title}")

    def str(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def repr(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"