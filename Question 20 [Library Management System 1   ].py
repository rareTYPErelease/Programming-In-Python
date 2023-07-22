# Define the Book class
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
       
    # Check whether the book is available or not
    def available(self, available_book):
        if available_book:
            print("Book available")
        else:
            print("Book not available")
            
    # Display all the information inputted by the borrower
    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)

# Input book information
title = input("Input book title: ")
author = input("Input author name: ")
publication_year = int(input("Enter publication year: "))

# Input whether the book has been returned or not (true/false)
available_book = input("Enter whether the book has been returned or not (true/false):")
available_book = available_book.lower() == 'true'

# Create a Book object with the provided information
book = Book(title, author, publication_year)

# Display book information
book.display_info()

# Check if the book is available
book.available(available_book)
