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


if __name__ == "__main__":
    my_library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a Book")
        print("2. Display Books")
        print("3. Find a Book")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            year = input("Enter the year of publication: ")
            book = Book(title, author, year)
            my_library.add_book(book)

        elif choice == '2':
            my_library.display_books()

        elif choice == '3':
            title = input("Enter the title of the book to find: ")
            my_library.find_book(title)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")