"""
Displays the menu for the personal library application.
This menu is invoked by the main function in the personal_library.py file.

Parameters:
    None
Returns:
    output
"""
import json

def display_menu():
    print("Please select an option (1-6):")
    print("------------------------")
    print("1. Add Book Title")
    print("2. Remove Book Title")
    print("3. List Book Titles")
    print("4. Search Book Title")
    print("5. Show Author Statistics")
    print("6. Save and Exit")
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

def list_all_books(library):
    books = []

    for book_title in library:
        book_author = library[book_title]["book_author"]
        book_year = library[book_title]["book_year"]

        books.append((book_title, book_author, book_year))

    return books

"""
Searches fors books in the library by their title.
Prompts user to search for title to find matching books.

Parameters:
    library
Returns:
    books
"""
def search_books(library):
    search_title = input("Enter the book title to search: ")
    books = []

    for book_title in library:
        if search_title.lower() in book_title.lower():
            book_author = library[book_title]["book_author"]
            book_year = library[book_title]["book_year"]

            books.append((book_title, book_author, book_year))

    return books

"""
Shows the numbers of books per authur in the library.

Parameters:
    library
Returns:
    statistics
"""
def author_statistics(library):
    statistics = {}

    for book_title in library:
        book_author = library[book_title]["book_author"]

        if book_author in statistics:
            statistics[book_author] += 1
        else:
            statistics[book_author] = 1

    return statistics

"""
Load library from JSON file.
Returns empty if rhe file is not found/

Parameters:
    None
Returns:
    library
"""
def load_library():
    try:
        with open("library_data.json", "r") as file:
            library = json.load(file)

        print(f"Loaded {len(library)} book(s) from library_data.json.")
        return library
    
    except (json.JSONDecodeError, FileNotFoundError):
        pass

    print(f"Loaded 0 books from library_data.json.")
    return{}

"""
Saves the current library to a JSON file.
Parameters:
    library
Returns:
    None
"""
def save_library(library):
    with open("library_data.json", "w") as file:
        json.dump(library, file, indent=4)
        
    print("Library saved to library_data.json.")
         
"""
Main control loops for personal library.
Processes user choices and saves the library before exiting.
Parameters:
    None
Returns:
    None
"""
def main():
    library = load_library()
    keep_running = True

    while keep_running:
        option = display_menu()

        if option == "1":
            add_book_title(library)
        elif option == "2":
            remove_a_book(library)
        elif option == "3":
            books = list_all_books(library)
            for book_title, book_author, book_year in books:
                print(f"{book_title} by {book_author} ({book_year})")
        elif option == "4":
            books = search_books(library)
            if books:
                for book_title, book_author, book_year in books:
                    print(f"{book_title} by {book_author} ({book_year})")
            else:
                print("No books were found.")   
        elif option == "5":
            statistics = author_statistics(library)
            print("Books per author:")
            for book_author in statistics:
                print(f"{book_author}: {statistics[book_author]}")
        elif option == "6":
            save_library(library)
            keep_running = False
        else:
            print("Invalid Choice. Please enter (1, 2, 3, 4, 5, or 6)")

if __name__ == "__main__":
    main()
