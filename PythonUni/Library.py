class Book :
    def __init__(self, title, author, year, copies) :
        self.title = title
        self.year = year
        self.author = author
        self.copies = copies

        self.is_borrowed = False
        self.borrower = None

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Author: {self.author}")
        print(f"Copies: {self.copies}")

class Library :

    def __init__(self) :
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def search_book_by_author(self, author):
        result = []
        for book in self.books:
            if book.author == author:
                result.append(book)
        if not result:
            print(f"No books found for this {author}")
        return result

    def display_books(self):
        if not self.books:
            print("No books in library!")
            return
        for book in self.books:
            book.display_info()

class LibraryMember :
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, library, title):
        book = library.search_book_by_title(title)
        if book is None:
            print("Book not found!")
            return
        if book.copies > 0:
            self.borrowed_books.append(book)
            book.copies -= 1
            print(f"- {self.name} borrowed '{book.title}'")
        else:
            print("No copies available for this book.")

    def return_book(self, library, title):
        book = library.search_book_by_title(title)
        if book is None:
            print("Book not found.")
            return
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.copies += 1
            print(f"{self.name} returned {book.title}")
        else:
            print(f"This {self.name} did not borrow {book.title}")

    def display_borrowed_books(self):
        print(f"Borrowed books by -> {self.name} ✔️")
        for book in self.borrowed_books:
            print(f"{book.title} by {book.author} ({book.year})")


library = Library()

book1 = Book("Python Programming", "John Smith", 2020, 5)
book2 = Book("Data Structures and Algorithms", "Alice Johnson", 2019, 3)

library.add_book(book1)
library.add_book(book2)

member1 = LibraryMember("David", "001")
member2 = LibraryMember("Emma", "002")

library.add_member(member1)
library.add_member(member2)

find_book = library.search_book_by_title("Python Programming")
if find_book is not None:
    find_book.display_info()
else:
    print("Book not found")

member1.borrow_book(library, "Python Programming")
member1.borrow_book(library, "Data Structures and Algorithms")

member1.display_borrowed_books()

library.display_books()