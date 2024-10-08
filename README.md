# Library Management System: Instruction Manual
Welcome to Eli's Library Management System! This command-line-based application is designed to help you manage a library's collection of books, users, and authors. This manual will guide you through setting up, running the application, and understanding its features.

# 1. Getting Started
Step 1: Setup Your Environment
Install Python: Ensure you have Python installed on your system. You can download it from python.org.
Create a Project Folder: 
Create a folder on your computer where you will store the application files. 
You can name it LibraryManagementSystem.

Step 2: Organize the Project Files
Inside the LibraryManagementSystem folder, create the following Python files:

1. book.py
2. user.py
3. author.py
4. library.py
5. main.py
6. connect_mysql.py

Copy and paste the code provided into the respective files.

# Step 3: Set Up the MySQL Database
Open MySQL Workbench or Command-Line Interface:

Use MySQL Workbench or the command-line interface to connect to your MySQL server.
Create the Database:

Run the following SQL command to create the database:

CREATE DATABASE library_management;
Use the Database:

Switch to the newly created database:
USE library_management;
Create the Required Tables:

Run the following SQL commands to create the necessary tables:

# Books Table:
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    genre VARCHAR(100),
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

# Authors Table:
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

# Users Table:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

# Borrowed Books Table:
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

# Verify Table Creation:
You can verify that the tables have been created by running:
SHOW TABLES;

Step 4: Running the Application
Open Terminal/Command Prompt: Navigate to the LibraryManagementSystem directory using the terminal or command prompt.

Example command: cd path/to/LibraryManagementSystem
Run the Application: Execute the main.py script to start the application.

Example command: python main.py

# 2. Application Features
Main Menu
Once the application starts, you will see the following main menu options:

Book Operations: Manage the library's book collection.
User Operations: Manage library users.
Author Operations: Manage book authors.
Quit: Exit the application.
You can select any option by entering the corresponding number.

# 2.1 Book Operations
1. Add a New Book: Allows you to add a new book to the library by entering details like the title, author ID, genre, publication date, and ISBN.
2. Borrow a Book: Allows a user to borrow a book. You need to enter the book ID and the user's library ID.
3. Return a Book: Allows a user to return a borrowed book. You need to enter the book ID and the user's library ID.
4. Search for a Book: Allows you to search for a book by title and view its details.
5. Display All Books: Displays a list of all books in the library along with their availability status.

# 2.2 User Operations
When you select "User Operations" from the main menu, the following options are available:

1. Add a New User: Allows you to add a new user to the library by entering their name and assigning a library ID.
2. View User Details: Allows you to view details of a specific user by entering their library ID.
3. Display All Users: Displays a list of all users registered in the library.

# 2.3 Author Operations
When you select "Author Operations" from the main menu, the following options are available:

1. Add a New Author: Allows you to add a new author to the system by entering their name and biography.
2. View Author Details: Allows you to view details of a specific author by entering their name.
3. Display All Authors: Displays a list of all authors registered in the library.

# 2.4 Quit
Selecting "Quit" will exit the application. Make sure to save your work or any necessary data before quitting.

# 3. Error Handling and Input Validation
The application is designed to handle errors gracefully. If you enter invalid data (e.g., a book that doesn’t exist or an incorrect user ID), the system will provide an error message and prompt you to try again.

Examples:

1. Invalid Menu Choice: If you enter a number outside the available options, you will be prompted to enter a valid choice.
2. Non-existent Book/User: If you attempt to borrow or return a book that isn’t in the system, or for a user who isn’t registered, the application will inform you of the issue.

4. Conclusion

# 4. Conclusion
The Library Management System is a simple yet powerful tool for managing a library’s books, users, and authors. By following this manual, you should be able to set up, run, and effectively use the application. The modular design of the code also makes it easy to expand with new features as needed.

If you have any questions or encounter issues, feel free to revisit the manual for guidance. Thank you, and I hope you enjoy using Eli's Library Management System!






