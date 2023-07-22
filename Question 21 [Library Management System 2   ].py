# Define the LibraryMember class
class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # List to store the borrowed books
        
    def borrow_book(self, book):
        self.borrowed_books.append(book)  # Add the book to the list of borrowed books
        
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)  # Remove the book from the list of borrowed books if it exists
            
    def display_info(self):
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("Number of borrowed books:", len(self.borrowed_books))  # Display the number of borrowed books

# Input member info
member_id = input("Input member ID: ")
name = input("Input member name: ")

# Create a new instance of the LibraryMember class for each library member
member = LibraryMember(member_id, name)

# Define the Book class
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        
    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)

# Input book info
title = input("Input book title: ")
author = input("Input book author: ")
publication_year = int(input("Enter publication year: "))
book_object = Book(title, author, publication_year)

# Input the number of books borrowed
num_book = int(input("Input number of books borrowed: "))

# Borrow books
for _ in range(num_book):
    member.borrow_book(Book(title, author, publication_year))

# Display member information
member.display_info()

# Return a book
member.return_book(book_object)

# Display updated member information
member.display_info()
