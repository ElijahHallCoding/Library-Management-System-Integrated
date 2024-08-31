from mysql.connector import Error

class Book:
    def __init__(self, title, author_id, genre, publication_date):
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.publication_date = publication_date
        self.is_available = True

    # Static method to add a book to the database
    @staticmethod
    def add_book_to_db(connection, title, author_id, genre, publication_date, isbn):
        cursor = connection.cursor()
        try:
            query = """
            INSERT INTO books (title, author_id, genre, publication_date, isbn, availability) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (title, author_id, genre, publication_date, isbn, 1))  # 1 indicates available
            connection.commit()
            print(f"Book '{title}' added successfully.")
        except Error as e:
            print(f"Failed to add book: {e}")
        finally:
            cursor.close()

    # Static method to borrow a book from the database
    @staticmethod
    def borrow_book_from_db(connection, book_id):
        cursor = connection.cursor()
        try:
            query = "SELECT availability FROM books WHERE id = %s"
            cursor.execute(query, (book_id,))
            result = cursor.fetchone()

            if result is None:
                print(f"Book with ID {book_id} not found.")
                return

            availability = result[0]

            if availability:
                update_query = "UPDATE books SET availability = 0 WHERE id = %s"
                cursor.execute(update_query, (book_id,))
                connection.commit()
                print("Book borrowed successfully.")
            else:
                print("Book is not available.")
        except Error as e:
            print(f"Failed to borrow book: {e}")
        finally:
            cursor.close()

    # Static method to return a book to the database
    @staticmethod
    def return_book_to_db(connection, book_id):
        cursor = connection.cursor()
        try:
            query = "SELECT availability FROM books WHERE id = %s"
            cursor.execute(query, (book_id,))
            result = cursor.fetchone()

            if result is None:
                print(f"Book with ID {book_id} not found.")
                return

            update_query = "UPDATE books SET availability = 1 WHERE id = %s"
            cursor.execute(update_query, (book_id,))
            connection.commit()
            print("Book returned successfully.")
        except Error as e:
            print(f"Failed to return book: {e}")
        finally:
            cursor.close()