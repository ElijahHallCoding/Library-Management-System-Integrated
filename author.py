class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    # Display author details
    def display_details(self):
        print(f"Author: {self.__name}")
        print(f"Biography: {self.__biography}")