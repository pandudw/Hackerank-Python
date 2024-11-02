class Book:
    def __init__(self,title,author,year):
        self.title  = title
        self.author = author
        self.year   = year
    def __str__(self):
        return f'"{self.title}" by {self.author} in {self.year}'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print("Added:", {book})
    
    def __display_book(self):
        if not self.books:
            print("No book available")
            return

        print("Book available in this library")
        for book in self.books:
            print(book)
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f'Found: {book}')
                return
        print(f'Book with title "{title}" not found.')


