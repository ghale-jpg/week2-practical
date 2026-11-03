books = {}
borrowed_books = []

def get_integer(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Enter a number greater than or equal to {minimum}.")
        except ValueError:
            print("Please enter a valid whole number.")

def add_book():
    book_id = input("Enter book ID: ").strip()
    if not book_id or book_id in books:
        print("Book ID is empty or already exists.")
        return
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    if not title or not author:
        print("Title and author cannot be empty.")
        return
    copies = get_integer("Enter number of copies: ")
    books[book_id] = {"title": title, "author": author, "copies": copies}
    print("Book added successfully.")

def display_books():
    available = False
    for book_id, book in books.items():
        if book["copies"] > 0:
            print(f"{book_id} | {book['title']} | {book['author']} | Copies: {book['copies']}")
            available = True
    if not available:
        print("There are no books with available copies.")

def search_book():
    term = input("Enter a title or author to search: ").strip().lower()
    if not term:
        print("Search text cannot be empty.")
        return
    found = False
    for book_id, book in books.items():
        if term in book["title"].lower() or term in book["author"].lower():
            print(f"{book_id} | {book['title']} | {book['author']} | Available: {book['copies']}")
            found = True
    if not found:
        print("No matching book was found.")

def borrow_book():
    book_id = input("Enter book ID to borrow: ").strip()
    if book_id not in books:
        print("Book not found.")
        return
    if books[book_id]["copies"] <= 0:
        print("No copies are currently available.")
        return
    borrower = input("Enter borrower/student ID: ").strip()
    if not borrower:
        print("Borrower ID cannot be empty.")
        return
    books[book_id]["copies"] -= 1
    borrowed_books.append((borrower, book_id))
    print("Book borrowed successfully.")

def return_book():
    book_id = input("Enter book ID to return: ").strip()
    borrower = input("Enter borrower/student ID: ").strip()
    record = (borrower, book_id)
    if record not in borrowed_books:
        print("This borrower does not have that book recorded as borrowed.")
        return
    borrowed_books.remove(record)
    books[book_id]["copies"] += 1
    print("Book returned successfully.")

def display_unavailable_books():
    found = False
    for book_id, book in books.items():
        if book["copies"] == 0:
            print(f"{book_id} | {book['title']} | {book['author']}")
            found = True
    if not found:
        print("All books have at least one available copy.")

def display_totals():
    total_titles = 0
    available_copies = 0
    for book in books.values():
        total_titles += 1
        available_copies += book["copies"]
    print(f"Different book records: {total_titles}")
    print(f"Available copies: {available_copies}")
    print(f"Currently borrowed copies: {len(borrowed_books)}")

def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add a book")
        print("2. Display available books")
        print("3. Search by title or author")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Display books with no available copies")
        print("7. Display book and copy totals")
        print("8. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            display_unavailable_books()
        elif choice == "7":
            display_totals()
        elif choice == "8":
            print("Library system closed.")
            break
        else:
            print("Invalid choice. Please select 1-8.")

if __name__ == "__main__":
    main()
