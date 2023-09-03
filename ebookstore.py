import sqlite3

# Connect to the database
db = sqlite3.connect('database.db')

# Create a cursor object to interact with the database
cursor = db.cursor()

# Create the "books" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Author TEXT,
        Qty INTEGER
    )
''')
db.commit()  # Commit the table creation

# List of books to insert into the database
diff_books = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12)
]

# Insert the books into the "books" table
cursor.executemany('''
    INSERT INTO books (id, Title, Author, Qty)
    VALUES (?, ?, ?, ?)
''', diff_books)

def display_menu():
    # Display the menu options
    print("Menu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")

def enter_book():
    # Function to enter a new book into the database
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))

    cursor.execute('''
        INSERT INTO books (id, Title, Author, Qty)
        VALUES (?, ?, ?, ?)
    ''', (id, title, author, qty))
    db.commit()  # Commit the book entry

    print("Book entered successfully.")

def update_book():
    # Function to update the quantity of a book
    id = int(input("Enter book ID to update: "))
    qty = int(input("Enter new quantity: "))

    cursor.execute('''
        UPDATE books
        SET Qty = ?
        WHERE id = ?
    ''', (qty, id))
    db.commit()  # Commit the book update

    print("Book updated successfully.")

def delete_book():
    # Function to delete a book from the database
    id = int(input("Enter book ID to delete: "))

    cursor.execute('''
        DELETE FROM books
        WHERE id = ?
    ''', (id,))
    db.commit()  # Commit the book deletion

    print("Book deleted successfully.")

def search_books():
    # Function to search for books by title
    title = input("Enter book title to search: ")

    cursor.execute('''
        SELECT * FROM books
        WHERE Title LIKE ?
    ''', ('%' + title + '%',))

    books = cursor.fetchall()

    if len(books) > 0:
        print("Matching books found:")
        for book in books:
            print("ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Quantity:", book[3])
            print()
    else:
        print("No matching books found.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (0-4): ")

    if choice == '1':
        enter_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_books()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")

db.commit()  # Commit any remaining changes
db.close()  # Close the database connection
