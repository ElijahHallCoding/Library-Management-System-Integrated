from library import Library

def main_menu():
    print("\nWelcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")
    return input("Please choose an option (1-4): ")

def book_menu(library):
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
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            publication_date = input("Enter publication date: ")
            library.add_book(title, author, genre, publication_date)
        elif choice == "2":
            title = input("Enter book title to borrow: ")
            user_id = input("Enter user library ID: ")
            library.borrow_book(title, user_id)
        elif choice == "3":
            title = input("Enter book title to return: ")
            user_id = input("Enter user library ID: ")
            library.return_book(title, user_id)
        elif choice == "4":
            title = input("Enter book title to search: ")
            library.search_book(title)
        elif choice == "5":
            library.display_all_books()
        else:
            print("Invalid choice, please select a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

def user_menu(library):
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Please choose an option (1-3): ")

    try:
        if choice == "1":
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            library.add_user(name, library_id)
        elif choice == "2":
            user_id = input("Enter user library ID to view details: ")
            library.view_user_details(user_id)
        elif choice == "3":
            library.display_all_users()
        else:
            print("Invalid choice, please select a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

def author_menu(library):
    print("\nAuthor Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Please choose an option (1-3): ")

    try:
        if choice == "1":
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            library.add_author(name, biography)
        elif choice == "2":
            name = input("Enter author name to view details: ")
            library.view_author_details(name)
        elif choice == "3":
            library.display_all_authors()
        else:
            print("Invalid choice, please select a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    library = Library()

    while True:
        choice = main_menu()

        if choice == "1":
            book_menu(library)
        elif choice == "2":
            user_menu(library)
        elif choice == "3":
            author_menu(library)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main() 