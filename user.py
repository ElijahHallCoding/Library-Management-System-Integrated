from mysql.connector import Error

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    # Static method to add a user to the database
    @staticmethod
    def add_user_to_db(connection, name, library_id):
        cursor = connection.cursor()
        try:
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            cursor.execute(query, (name, library_id))
            connection.commit()
            print(f"User '{name}' added successfully.")
        except Error as e:
            print(f"Failed to add user: {e}")
        finally:
            cursor.close()

    # Static method to view user details
    @staticmethod
    def view_user_details(connection, library_id):
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM users WHERE library_id = %s"
            cursor.execute(query, (library_id,))
            user = cursor.fetchone()

            if user:
                print(f"User ID: {user[0]}, Name: {user[1]}, Library ID: {user[2]}")
            else:
                print("User not found.")
        except Error as e:
            print(f"Failed to retrieve user: {e}")
        finally:
            cursor.close()

    # Static method to display all users
    @staticmethod
    def display_all_users(connection):
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM users"
            cursor.execute(query)
            users = cursor.fetchall()

            if users:
                print("Users in the library system:")
                for user in users:
                    print(f"User ID: {user[0]}, Name: {user[1]}, Library ID: {user[2]}")
            else:
                print("No users found.")
        except Error as e:
            print(f"Failed to retrieve users: {e}")
        finally:
            cursor.close()