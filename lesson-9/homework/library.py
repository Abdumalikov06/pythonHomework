# Custom exceptions
class BookNotFoundException(Exception):
    """Raised when the book is not found in the library."""
    pass

class BookAlreadyBorrowedException(Exception):
    """Raised when the book is already borrowed."""
    pass

class MemberLimitExceededException(Exception):
    """Raised when a member tries to borrow more books than allowed."""
    pass

# Class to represent a Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Class to represent a Library Member
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print(f"{book} was not borrowed by {self.name}.")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"{self.name} has borrowed: {', '.join(borrowed_titles) if borrowed_titles else 'No books'}"

# Class to represent a Library
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book_title):
        # Find the book in the library
        book = next((b for b in self.books if b.title == book_title), None)
        
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book_title}' is already borrowed.")
        
        # Borrow the book
        book.is_borrowed = True
        member.borrow_book(book)
        print(f"{member.name} successfully borrowed '{book_title}'.")

    def return_book(self, member, book_title):
        # Find the book in the borrowed books of the member
        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        
        if not book:
            print(f"{member.name} did not borrow '{book_title}'.")
            return
        
        # Return the book
        book.is_borrowed = False
        member.return_book(book)
        print(f"{member.name} successfully returned '{book_title}'.")

# Test the system with some sample data and scenarios
def test_library_system():
    # Create the library
    library = Library()

    # Add some books to the library
    book1 = Book("The Catcher in the Rye", "J.D. Salinger")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    book4 = Book("Moby-Dick", "Herman Melville")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # Add some members to the library
    member1 = Member("Alice")
    member2 = Member("Bob")
    library.add_member(member1)
    library.add_member(member2)

    # Test borrowing books
    try:
        library.borrow_book(member1, "1984")  
        library.borrow_book(member1, "To Kill a Mockingbird") 
        library.borrow_book(member1, "Moby-Dick")  
        library.borrow_book(member1, "The Catcher in the Rye")  
    except MemberLimitExceededException as e:
        print(e)

    # Test borrowing a book that doesn't exist
    try:
        library.borrow_book(member2, "The Great Gatsby") 
    except BookNotFoundException as e:
        print(e)

    
    try:
        library.borrow_book(member2, "1984")  
    except BookAlreadyBorrowedException as e:
        print(e)

    
    library.return_book(member1, "1984")  
    library.return_book(member2, "1984") 
    
    print(member1)
    print(member2)

# Run the test
test_library_system()
