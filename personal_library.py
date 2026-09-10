"""
Displays the menu for the personal library application.
This menu is invoked by the main function in the personal_library.py file.

Parameters:
    None
Returns:
    None
"""


def display_menu():
    print("Please select an option:")
    print("------------------------")
    print("1. Add Book Title")
    print("2. Remove Book Title")
    print("3. List Book Titles")
    print("4. Search Book Title")
    print("5. Exit")
    print("")


def main():
    display_menu()

if __name__ == "__main__":
    main()
