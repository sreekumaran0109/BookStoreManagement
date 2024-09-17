import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="sree",
    password="root"
)

mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE IF NOT EXISTS store")
mycursor.execute("USE store")


mycursor.execute("""
CREATE TABLE IF NOT EXISTS signup (
    username VARCHAR(20) PRIMARY KEY,
    password VARCHAR(20)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Available_Books (
    BookName VARCHAR(30) PRIMARY KEY,
    Genre VARCHAR(20),
    Quantity INT(3),
    Author VARCHAR(20),
    Publication VARCHAR(30),
    Price INT(4)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Sell_rec (
    CustomerName VARCHAR(20),
    PhoneNumber CHAR(10) UNIQUE,
    BookName VARCHAR(30),
    Quantity INT(3),
    Price INT(4),
    Total_Amount INT(6),
    FOREIGN KEY (BookName) REFERENCES Available_Books(BookName)
)
""")

while True:
    print("\n\n1:Signup 2:Login")
    ch = int(input("SIGNUP/LOGIN(1,2):"))

    if ch == 1:  # Signup
        username = input("USERNAME:")
        pw = input("PASSWORD:")
        mycursor.execute("INSERT INTO signup (username, password) VALUES (%s, %s)", (username, pw))
        mydb.commit()
        print("Signup successful!")

    elif ch == 2:  # Login
        username = input("USERNAME:")
        mycursor.execute("SELECT username FROM signup WHERE username = %s", (username,))
        pot = mycursor.fetchone()
        
        if pot is not None:
            pw = input("PASSWORD:")
            mycursor.execute("SELECT password FROM signup WHERE username = %s AND password = %s", (username, pw))
            a = mycursor.fetchone()
            
            if a is not None:
                print("LOGIN SUCCESSFUL")
                print("MY BOOK STORE")

                while True:
                    print("\n\n1:Add Books \n2:Sell Books \n3:Search Books \n4:Sell Record \n5:Available Books \n6:Total Income after the Latest Reset  \n7:Exit")
                    a = int(input("Enter your choice:"))

                    if a == 1:  # Add Books
                        print("\nAll information prompted are mandatory to be filled\n")
                        book = input("Enter Book Name:")
                        genre = input("Genre:")
                        quantity = int(input("Enter quantity:"))
                        author = input("Enter author name:")
                        publication = input("Enter publication house:")
                        price = int(input("Enter the price:"))

                        mycursor.execute("SELECT * FROM Available_Books WHERE BookName = %s", (book,))
                        row = mycursor.fetchone()

                        if row is not None:
                            mycursor.execute("UPDATE Available_Books SET Quantity = Quantity + %s WHERE BookName = %s", (quantity, book))
                            mydb.commit()
                            print("SUCCESSFULLY UPDATED")
                        else:
                            mycursor.execute("INSERT INTO Available_Books (BookName, Genre, Quantity, Author, Publication, Price) VALUES (%s, %s, %s, %s, %s, %s)",
                                             (book, genre, quantity, author, publication, price))
                            mydb.commit()
                            print("SUCCESSFULLY ADDED")

                    elif a == 2:  # Sell Books
                        print("AVAILABLE BOOKS...")
                        mycursor.execute("SELECT * FROM Available_Books")
                        for x in mycursor:
                            print(x)

                        cusname = input("Enter customer name:")
                        phno = input("Enter phone number:")
                        book = input("Enter Book Name:")
                        quantity = int(input("Enter quantity:"))

                        mycursor.execute("SELECT Price, Quantity FROM Available_Books WHERE BookName = %s", (book,))
                        result = mycursor.fetchone()

                        if result:
                            price, available_quantity = result
                            if available_quantity < quantity:
                                print(f"{quantity} Books are not available!!!!")
                            else:
                                total_amount = price * quantity
                                mycursor.execute("INSERT INTO Sell_rec (CustomerName, PhoneNumber, BookName, Quantity, Price, Total_Amount) VALUES (%s, %s, %s, %s, %s, %s)",
                                                 (cusname, phno, book, quantity, price, total_amount))
                                mycursor.execute("UPDATE Available_Books SET Quantity = Quantity - %s WHERE BookName = %s", (quantity, book))
                                mydb.commit()
                                print("BOOK HAS BEEN SOLD")
                        else:
                            print("BOOK IS NOT AVAILABLE!!")

                    elif a == 3:  # Search Books
                        print("1:Search by name \n2:Search by genre \n3:Search by author")
                        l = int(input("Search by?:"))

                        if l == 1:  # By Book Name
                            o = input("Enter Book to search:")
                            mycursor.execute("SELECT BookName FROM Available_Books WHERE BookName = %s", (o,))
                            tree = mycursor.fetchone()
                            if tree:
                                print("BOOK IS IN STOCK")
                            else:
                                print("BOOK IS NOT IN STOCK!!")

                        elif l == 2:  # By Genre
                            g = input("Enter genre to search:")
                            mycursor.execute("SELECT * FROM Available_Books WHERE Genre = %s", (g,))
                            poll = mycursor.fetchall()
                            if poll:
                                print("BOOKS OF SUCH GENRE ARE AVAILABLE")
                                for y in poll:
                                    print(y)
                            else:
                                print("BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!")

                        elif l == 3:  # By Author Name
                            au = input("Enter author to search:")
                            mycursor.execute("SELECT * FROM Available_Books WHERE Author = %s", (au,))
                            home = mycursor.fetchall()
                            if home:
                                print("BOOKS BY THIS AUTHOR ARE AVAILABLE")
                                for z in home:
                                    print(z)
                            else:
                                print("BOOKS OF THIS AUTHOR ARE NOT AVAILABLE!!!")
                        mydb.commit()

                    elif a == 4:  # Sell Record
                        print("1:Sell history details")
                        print("2:Reset Sell history")
                        ty = int(input("Enter your choice:"))

                        if ty == 1:
                            mycursor.execute("SELECT * FROM Sell_rec")
                            for u in mycursor:
                                print(u)

                        elif ty == 2:
                            bb = input("Are you sure(Y/N):")
                            if bb.upper() == "Y":
                                mycursor.execute("DELETE FROM Sell_rec")
                                mydb.commit()

                    elif a == 5:  # Available Books
                        mycursor.execute("SELECT * FROM Available_Books ORDER BY BookName")
                        for v in mycursor:
                            print(v)

                    elif a == 6:  # Total Income after Latest Update
                        mycursor.execute("SELECT SUM(Total_Amount) FROM Sell_rec")
                        total_income = mycursor.fetchone()[0]
                        print(f"Total income after latest update: {total_income}")

                    elif a == 7:  
                        print("\nThank you")
                        break

                break 

            else:
                print("INCORRECT PASSWORD")

        else:
            print("INVALID USERNAME")

    else:
        break
