# Project Name

Bookstore

## Description

This application allows book store owners to manage the contents of their store a lot easier. 
It can be used to catalogue and add new items to the store. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Credits](#credits)

## Installation

Download the .py file and be sure to install an application that is able to run the .py file. 
Once done all you will need to is hit run and follow the instruction to assist in what you plan to use the application for. 

You should have Python installed on your system.

Ensure you have the sqlite3 library installed. If it's not installed, you can usually install it using pip in CMD:

pip install sqlite3


## Usage

onnect to the Database:

The script connects to an SQLite database named 'database.db' by default. You can change this by modifying the following line:

python

db = sqlite3.connect('database.db')
Creating the "books" Table:

The script creates a table called "books" in the database if it doesn't already exist. This table will store information about the books, including ID, Title, Author, and Quantity.

Inserting Sample Books (Optional):

By default, the script inserts a list of sample books into the "books" table. You can modify the diff_books list to add your own books or remove the sample books.

Display Menu:

When you run the script, it will display a menu with the following options:

markdown

Menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
Using the Menu:

Enter book (Option 1): Allows you to enter a new book into the database. Follow the prompts to enter the book's ID, title, author, and quantity.

Update book (Option 2): Lets you update the quantity of a book. Provide the book's ID and the new quantity.

Delete book (Option 3): Allows you to delete a book from the database. Provide the book's ID to delete it.

Search books (Option 4): Enables you to search for books by title. Enter a partial or full title, and the script will display matching books.

Exit (Option 0): Exits the script.

Main Program Loop:

The script runs in a loop, allowing you to perform multiple actions in succession. It will keep executing until you choose to exit (Option 0).

Commit Changes and Close Database:

The script commits any changes you make to the database, including adding, updating, or deleting books, before closing the database connection.

Example Usage:
Here are some example scenarios to help you get started:

Scenario 1: Entering a New Book

Choose option 1 from the menu.
Enter the book's ID, title, author, and quantity as prompted.
The script will add the book to the database, and you'll see a confirmation message.
Scenario 2: Updating a Book's Quantity

Choose option 2 from the menu.
Enter the book's ID that you want to update.
Enter the new quantity for the book.
The script will update the book's quantity, and you'll see a confirmation message.
Scenario 3: Deleting a Book

Choose option 3 from the menu.
Enter the book's ID that you want to delete.
The script will remove the book from the database, and you'll see a confirmation message.
Scenario 4: Searching for Books

Choose option 4 from the menu.
Enter a partial or full title of the book you want to search for.
The script will display a list of matching books.
Remember that you can always exit the script by choosing option 0.

### Screenshots
![image](https://github.com/Matthigg1998/Bookstore/assets/143545116/b6b9eafc-bd6a-46d7-b247-c04feb65deae)
![image](https://github.com/Matthigg1998/Bookstore/assets/143545116/29c0b828-30dc-49a1-b58e-bc6bd16a5f46)
![image](https://github.com/Matthigg1998/Bookstore/assets/143545116/7b13643f-aa42-46ec-a3b9-dbfa93b9ec88)
![image](https://github.com/Matthigg1998/Bookstore/assets/143545116/9fba4a61-4792-464d-bff9-ecc8ca3695b4)
![image](https://github.com/Matthigg1998/Bookstore/assets/143545116/e8ced103-3b2a-455f-b055-871fc578ae21)

## Credits

- Matthew Higgins https://github.com/Matthigg1998


