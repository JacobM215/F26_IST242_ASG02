"""
Displays the menu for the personal library application.
This menu is invoked by the main function in the personal_library.py file.

Parameters:
    None
Returns:
    output
"""

def display_menu():
    print("Please select an option (1-5):")
    print("------------------------")
    print("1. Add Book Title")
    print("2. Remove Book Title")
    print("3. List Book Titles")
    print("4. Search Book Title")
    print("5. Exit")
    print()

    option = input("Enter your choice: ")
    return option

"""
Allows user to enter book title, author, and year it was published.
The option is invoked when the user's input = 1.

Parameters:
    library
Returns:
    None
"""

def add_book_title(library):
    
    book_title = input("Enter the book title to add: ")
    book_author = input("Enter the author: ")
    book_year = input("Enter the year of the book: ")

    library[book_title] = {
        "book_author": book_author,
        "book_year": book_year 
    }

    print(f"'{book_title}' has been added to your personal library.")

"""
Allows user to remove an existing book title, fails if not found.
The option is invoked when the user's input = 2.

Parameters:
    library
Returns:
    None
"""

def remove_a_book(library):
    book_title = input("Enter the book title: ")

    if book_title in library:
        del library[book_title]
        print(f"'{book_title}' has been removed from your personal library.")
    else:
        print(f"'{book_title}' was not found in your personal library.")

def main():
    library = {}
    keep_running = True

    while keep_running:
        option = display_menu()

        if option == "1":
            add_book_title(library)
        elif option == "2":
            remove_a_book(library)
        else:
            print("Invalid Choice. Please enter (1, 2, 3, 4, or 5)")

if __name__ == "__main__":
    main()
