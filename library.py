import mysql.connector
from connect_mysql import connect_database

class Library:
    def __init__(self):
        self.conn = connect_database()
        self.cursor = self.conn.cursor()

    # Method to add a book to the library
    def add_book(self, title, author, genre, publication_date, isbn):
        try:
            # Check if the author exists
            self.cursor.execute("SELECT id FROM authors WHERE name = %s", (author,))
            author_id = self.cursor.fetchone()
            if not author_id:
                print(f"Error: Author '{author}' not found.")
                return

            # Insert the book into the database
            self.cursor.execute(
                "INSERT INTO books (title, author_id, genre, publication_date, isbn) VALUES (%s, %s, %s, %s, %s)",
                (title, author_id[0], genre, publication_date, isbn)
            )
            self.conn.commit()
            print(f"Book '{title}' added successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # Method to borrow a book from the library
    def borrow_book(self, title, user_id):
        try:
            # Check if the book exists and is available
            self.cursor.execute("SELECT id, availability FROM books WHERE title = %s", (title,))
            book = self.cursor.fetchone()
            if not book:
                print(f"Error: Book '{title}' not found.")
                return
            if not book[1]:
                print(f"Error: Book '{title}' is currently unavailable.")
                return

            # Check if the user exists
            self.cursor.execute("SELECT id FROM users WHERE library_id = %s", (user_id,))
            user = self.cursor.fetchone()
            if not user:
                print(f"Error: User with ID '{user_id}' not found.")
                return

            # Insert into borrowed_books table
            self.cursor.execute(
                "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())",
                (user[0], book[0])
            )
            self.conn.commit()

            # Mark the book as unavailable
            self.cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book[0],))
            self.conn.commit()

            print(f"Book '{title}' borrowed by User ID '{user_id}'.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # Method to close the database connection
    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("MySQL connection closed.")