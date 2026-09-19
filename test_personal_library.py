# virtual enviroment
from personal_library import display_menu, add_book_title, main

# Tests if display_menu function works
def test_display_menu_add_book(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")

    option = display_menu()

    assert option == "1"

# Tests the add_book_title function
def test_add_book_title(monkeypatch):
    inputs = iter(["The Hobbit", "J.R.R. Tolkien", "1937"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    library = {}

    add_book_title(library)

    assert "The Hobbit" in library
    assert library["The Hobbit"]["book_author"] == "J.R.R. Tolkien"
    assert library["The Hobbit"]["book_year"] == "1937"

# Test to see if a different book can be added 
def test_add_different_book(monkeypatch):
    inputs = iter(["1984", "George Orwell", "1949"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    library = {}

    add_book_title(library)

    assert "1984" in library
    assert library["1984"]["book_author"] == "George Orwell"
    assert library["1984"]["book_year"] == "1949"

# Test if book updates or duplicates
def test_duplicate_book_title(monkeypatch):
    inputs = iter([
        "The Hobbit",
        "J.R.R. Tolkien",
        "1937",
        "The Hobbit",
        "Different Author",
        "2020"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    library = {}

    add_book_title(library)
    add_book_title(library)

    assert len(library) == 1
    assert library["The Hobbit"]["book_author"] == "Different Author"
    assert library["The Hobbit"]["book_year"] == "2020"