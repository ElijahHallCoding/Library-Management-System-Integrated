from mysql.connector import Error

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    # Static method to add author to the database
    @staticmethod
    def add_author_to_db(connection, name, biography):
        cursor = connection.cursor()
        try:
            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, (name, biography))
            connection.commit()
            print(f"Author '{name}' added successfully.")
        except Error as e:
            print(f"Failed to add author: {e}")
        finally:
            cursor.close()

    # Static method to view author details
    @staticmethod
    def view_author_details(connection, name):
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM authors WHERE name = %s"
            cursor.execute(query, (name,))
            author = cursor.fetchone()

            if author:
                print(f"Author ID: {author[0]}, Name: {author[1]}, Biography: {author[2]}")
            else:
                print("Author not found.")
        except Error as e:
            print(f"Failed to retrieve author: {e}")
        finally:
            cursor.close()

    # Static method to display all authors
    @staticmethod
    def display_all_authors(connection):
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM authors"
            cursor.execute(query)
            authors = cursor.fetchall()

            if authors:
                print("Authors in the library system:")
                for author in authors:
                    print(f"Author ID: {author[0]}, Name: {author[1]}, Biography: {author[2]}")
            else:
                print("No authors found.")
        except Error as e:
            print(f"Failed to retrieve authors: {e}")
        finally:
            cursor.close()