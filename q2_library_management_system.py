# q2_library_system.py

# Store the library catalog as a dictionary
# key = book_id (int)
# value = tuple (title, author, year)
catalog = {}

# Maintain a list called borrowed_books to track currently issued book IDs
borrowed_books = []

# Maintain a set called members to store unique member IDs
members = set()


def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print("Book added successfully.")


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print("Book borrowed successfully.")
        else:
            print("Book already borrowed.")
    else:
        print("Book does not exist.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book returned successfully.")
    else:
        print("Book was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            print(book_id, details)


def main():
    add_book(catalog, 101, "The Alchemist", "Paulo Coelho", 1988)
    add_book(catalog, 102, "Harry Potter", "J.K. Rowling", 1997)
    add_book(catalog, 103, "The Hobbit", "J.R.R. Tolkien", 1937)
    add_book(catalog, 104, "Atomic Habits", "James Clear", 2018)

    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 2)

    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    return_book(borrowed_books, 101)

    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()