# Book Store Management System

This Python application provides a simple Book Store Management System using MySQL for data storage. It allows users to sign up, log in, manage books, track sales, and handle staff details.

## Features

-   **User Authentication:**
    -      Signup: Allows new users to create accounts with a username and password.
    -      Login: Verifies user credentials to grant access to the system.
-   **Book Management:**
    -      Add Books: Adds new books to the inventory, updating quantities if the book already exists.
    -      Delete Books (Sell): Simulates selling books, updating inventory, and recording sales.
    -      Search Books: Searches for books by name, genre, or author.
    -      Available Books: Displays a list of all available books.
-   **Sales Tracking:**
    -      Sell Record: Stores records of book sales, including customer details and book information.
    -      Total Income: Calculates and displays the total income from book sales.
    -   Reset Sell history: Deletes all the records from sell history.
-   **Staff Management:**
    -      Add Staff: Adds new staff member details.
    -      Remove Staff: Removes existing staff member details.
    -      Staff Details: Displays details of all staff members.

## Prerequisites

-   Python 3.x
-   MySQL Server
-   `mysql-connector-python` library (Install using `pip install mysql-connector-python`)

## Setup

1.  **Install Dependencies:**

    ```bash
    pip install mysql-connector-python
    ```

2.  **MySQL Setup:**
    -   Ensure you have a running MySQL server.
    -   Create a user with necessary privileges. In the code provided the user is root with password kvafs123. Please change these credentials.
    -   The script creates a database named `store` and tables within it.

3.  **Run the Application:**

    ```bash
    python your_script_name.py
    ```

    (Replace `your_script_name.py` with the actual name of your Python script.)

## Usage

1.  **Signup/Login:**
    -      The application prompts you to either sign up or log in.
    -      Follow the on-screen instructions to create an account or log in.

2.  **Main Menu:**
    -      After successful login, you'll see the main menu with options to manage books, staff, sales, and more.
    -      Enter the corresponding number to select an option.
    -   Follow the prompts to perform the chosen operation.

3.  **Book Operations:**
    -      Add books by entering book details.
    -      Sell books by entering customer and book details.
    -      Search for books using the provided search options.
    -   View available books.

4.  **Staff Operations:**
    -   Add, remove or view staff details.

5.  **Sales Operations:**
    -   View sell history or reset it.
    -   View total income.

## Database Structure

-   **`store` Database:**
    -   **`signup` Table:**
        -   `username` (VARCHAR(20))
        -   `password` (VARCHAR(20))
    -   **`Available_Books` Table:**
        -   `BookName` (VARCHAR(30) PRIMARY KEY)
        -   `Genre` (VARCHAR(20))
        -   `Quantity` (INT(3))
        -   `Author` (VARCHAR(20))
        -   `Publication` (VARCHAR(30))
        -   `Price` (INT(4))
    -   **`Sell_rec` Table:**
        -   `CustomerName` (VARCHAR(20))
        -   `PhoneNumber` (CHAR(10) UNIQUE KEY)
        -   `BookName` (VARCHAR(30) FOREIGN KEY referencing `Available_Books`)
        -   `Quantity` (INT(100))
        -   `Price` (INT(4))
    -   **`Staff_details` Table:**
        -   `Name` (VARCHAR(30))
        -   `Gender` (VARCHAR(10))
        -   `Age` (INT(3))
        -   `PhoneNumber` (CHAR(10) UNIQUE KEY)
        -   `Address` (VARCHAR(40))

## Security Considerations
