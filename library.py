from book import Book
from user import User
from author import Author

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.authors = {}

    # Book operations
    def add_book(self, title, author, genre, publication_date):
        title_key = title.lower()
        if title_key in self.books:
            print("Error: Book already exists.")
        else:
            new_book = Book(title, author, genre, publication_date)
            self.books[title_key] = new_book
            print(f"Book '{title}' added successfully.")

    def borrow_book(self, title, user_id):
        title_key = title.lower()
        if user_id not in self.users:
            raise ValueError("Error: Invalid user ID.")
        try:
            if title_key in self.books:
                book = self.books[title_key]
                user = self.users[user_id]
                if book.borrow_book():
                    user.borrow_book(title)
                    print(f"Book '{title}' borrowed by {user.get_name()}.")
                else:
                    print(f"Error: Book '{title}' is currently unavailable.")
            else:
                print("Error: Invalid book title.")
        except KeyError:
            print("Error: Book or user not found.")

    def return_book(self, title, user_id):
        title_key = title.lower()
        if user_id not in self.users:
            raise ValueError("Error: Invalid user ID.")
        try:
            if title_key in self.books:
                book = self.books[title_key]
                user = self.users[user_id]
                if title in user.get_borrowed_books():
                    book.return_book()
                    user.return_book(title)
                    print(f"Book '{title}' returned by {user.get_name()}.")
                else:
                    print(f"Error: {user.get_name()} has not borrowed '{title}'.")
            else:
                print("Error: Invalid book title.")
        except KeyError:
            print("Error: Book or user not found.")

    def search_book(self, title):
        title_key = title.lower()
        try:
            if title_key in self.books:
                self.books[title_key].display_details()
            else:
                print("Error: Book not found.")
        except KeyError:
            print("Error: Book not found.")

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books.values():
                book.display_details()

    # User operations
    def add_user(self, name, library_id):
        if library_id in self.users:
            print("Error: User already exists.")
        else:
            new_user = User(name, library_id)
            self.users[library_id] = new_user
            print(f"User '{name}' added successfully.")

    def view_user_details(self, user_id):
        try:
            if user_id in self.users:
                self.users[user_id].display_details()
            else:
                print("Error: User not found.")
        except KeyError:
            print("Error: User not found.")

    def display_all_users(self):
        if not self.users:
            print("No users found.")
        else:
            for user in self.users.values():
                user.display_details()

    # Author operations
    def add_author(self, name, biography):
        if name in self.authors:
            print("Error: Author already exists.")
        else:
            new_author = Author(name, biography)
            self.authors[name] = new_author
            print(f"Author '{name}' added successfully.")

    def view_author_details(self, name):
        try:
            if name in self.authors:
                self.authors[name].display_details()
            else:
                print("Error: Author not found.")
        except KeyError:
            print("Error: Author not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors found.")
        else:
            for author in self.authors.values():
                author.display_details()