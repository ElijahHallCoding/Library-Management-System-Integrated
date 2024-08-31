from connect_mysql import connect_database
from book import Book
from user import User
from author import Author

def book_menu(connection):
    print("\nBook Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Please choose an option (1-5): ")

    try:
        if choice == "1":
            title = input("Enter book title: ")
            author_id = input("Enter author ID: ")
            genre = input("Enter book genre: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            isbn = input("Enter ISBN: ")
            Book.add_book_to_db(connection, title, author_id, genre, publication_date, isbn)
        elif choice == "2":
            book_id = input("Enter book ID to borrow: ")
            Book.borrow_book_from_db(connection, book_id)
        elif choice == "3":
            book_id = input("Enter book ID to return: ")
            Book.return_book_to_db(connection, book_id)
        elif choice == "4":
            title = input("Enter book title to search: ")
            search_book_in_db(connection, title)
        elif choice == "5":
            display_all_books_in_db(connection)
        else:
            print("Invalid choice, please select a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

def user_menu(connection):
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Please choose an option (1-3): ")

    try:
        if choice == "1":
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            User.add_user_to_db(connection, name, library_id)
        elif choice == "2":
            user_id = input("Enter user library ID to view details: ")
            User.view_user_details(connection, user_id)
        elif choice == "3":
            User.display_all_users(connection)
        else:
            print("Invalid choice, please select a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

def author_menu(connection):
    print("\nAuthor Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Please choose an option (1-3): ")

    try:
        if choice == "1":
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            Author.add_author_to_db(connection, name, biography)
        elif choice == "2":
            name = input("Enter author name to view details: ")
            Author.view_author_details(connection, name)
        elif choice == "3":
            Author.display_all_authors(connection)
        else:
            print("Invalid choice, please select a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Additional functions to handle searching and displaying books
def search_book_in_db(connection, title):
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM books WHERE title = %s"
        cursor.execute(query, (title,))
        book = cursor.fetchone()

        if book:
            print(f"Book Found: ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Genre: {book[3]}, "
                  f"Publication Date: {book[4]}, ISBN: {book[5]}, Availability: {'Available' if book[6] else 'Unavailable'}")
        else:
            print("Book not found.")
    except Error as e:
        print(f"Failed to search book: {e}")
    finally:
        cursor.close()

def display_all_books_in_db(connection):
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM books"
        cursor.execute(query)
        books = cursor.fetchall()

        if books:
            print("Books in Library:")
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Genre: {book[3]}, "
                      f"Publication Date: {book[4]}, ISBN: {book[5]}, Availability: {'Available' if book[6] else 'Unavailable'}")
        else:
            print("No books available.")
    except Error as e:
        print(f"Failed to display books: {e}")
    finally:
        cursor.close()

# Main function to run the program
def main():
    connection = connect_database()

    if connection:
        while True:
            print("\nMain Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Please choose an option (1-4): ")

            if choice == "1":
                book_menu(connection)
            elif choice == "2":
                user_menu(connection)
            elif choice == "3":
                author_menu(connection)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please select a valid option.")
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main()