# Book Store Management System

This is a Python-based Book Store Management System that interacts with a MySQL database. It provides functionalities for user signup, login, managing book inventory, selling books, and viewing sales records. The project uses the `mysql-connector` Python library to interact with a MySQL database.

## Features
- **User Signup & Login**: 
  - Users can sign up with a username and password.
  - Users can log in using their credentials.
  
- **Book Inventory Management**: 
  - Add new books to the inventory.
  - Update the quantity of books already available.
  - Search books by name, genre, or author.

- **Selling Books**:
  - Manage book sales by entering customer details and book information.
  - Automatically update the stock after selling books.
  
- **Sales Records**:
  - View sales history.
  - Reset sales records if needed.
  
- **Income Calculation**:
  - Calculate the total income after the latest reset.

## Prerequisites

Before running this project, you need to have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL](https://www.mysql.com/downloads/)
- `mysql-connector` Python library (`pip install mysql-connector-python`)

## Database Setup

1. The code automatically creates a MySQL database named `store` and the following tables if they don't already exist:
   - `signup`: stores user credentials (username and password).
   - `Available_Books`: stores book information (book name, genre, quantity, author, publication, and price).
   - `Sell_rec`: stores records of sold books (customer name, phone number, book name, quantity, price, and total amount).

## How to Run the Project

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/book-store-management.git
    ```

2. Navigate to the project directory:

    ```bash
    cd book-store-management
    ```

3. Install the required Python packages:

    ```bash
    pip install mysql-connector-python
    ```

4. Set up your MySQL server and update the connection details in the code if necessary:

    ```python
    mydb = mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password"
    )
    ```

5. Run the script:

    ```bash
    python Book_Store_Management.py
    ```

## Project Flow

- **Signup**: Enter a unique username and password to create a new account.
- **Login**: Enter your username and password to access the system.
- **Book Management**: Once logged in, you can manage book inventory (add or update books), sell books, view sales history, reset sales records, and calculate total income.

## Example Usage
