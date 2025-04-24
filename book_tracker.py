import csv
import os
from datetime import datetime, timedelta

filename = "library_books.csv"
books = []

# Load the CSV
if os.path.exists(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            book = {
                "title": row[0],
                "author": row[1],
                "genre": row[2],
                "borrowed_date": row[3],
                "status": row[4]
            }
            books.append(book)

# Add book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    borrowed_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if not borrowed_date:
        borrowed_date = datetime.today().strftime("%Y-%m-%d")
    
    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "borrowed_date": borrowed_date,
        "status": "borrowed"
    }

    books.append(book)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([title, author, genre, borrowed_date, "borrowed"])

    print("Book added successfully!")

# Mark as returned
def mark_returned():
    title = input("Enter book title to mark as returned: ")

    found = False
    for book in books:
        if book["title"].lower() == title.lower() and book["status"] == "borrowed":
            book["status"] = "returned"
            found = True
            break

    if found:
        
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for book in books:
                writer.writerow([
                    book["title"],
                    book["author"],
                    book["genre"],
                    book["borrowed_date"],
                    book["status"]
                ])
        print("Book marked as returned.")
    else:
        print("Book not found or already returned.")

# List borrowed books
def list_borrowed():
   
    print("\n--- Borrowed Books ---")
    found = False
    for book in books:
        if book["status"] == "borrowed":
            print(f"{book['title']} | {book['author']} | {book['genre']} | {book['borrowed_date']}")

            found = True
    if not found:
        print("No borrowed books found.")

# Show overdue books
def show_overdue():
    print("\n--- Overdue Books ---")
    today = datetime.now().date()
    found = False
    for book in books:
        if book["status"] == "borrowed" and book.get("borrowed_date"):
            try:
                borrowed_date = datetime.strptime(book["borrowed_date"], "%Y-%m-%d").date()
                days_overdue = (today - borrowed_date).days - 3  # Assuming a 3-day borrowing period
                # Check if the book is overdue
                if days_overdue > 0:
                    print(f"{book['title']} | {book['borrowed_date']} | {days_overdue}d")
                    found = True
            except ValueError:
                print(f"Invalid date format for book: {book['title']}")
    if not found:
        print("No overdue books.")

# Main loop
while True:
    print("\n--- Library Book Tracker ---")
    print("Commands: add | return | list | overdue | exit")
    command = input("Enter command: ").lower()

    if command == "add":
        add_book()
    elif command == "return":
        mark_returned()
    elif command == "list":
        list_borrowed()
    elif command == "overdue":
        show_overdue()
    elif command == "exit":
        print("Exiting Library Tracker...")
        break
    else:
        print("Invalid command. Try again.")
