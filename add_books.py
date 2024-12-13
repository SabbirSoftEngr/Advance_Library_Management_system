from datetime import datetime
import save_all_books
import random

def add_book(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    while True:
        try:
            year = int(input("Enter Publishing Year: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            price = int(input("Enter Book Price: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            quantity = int(input("Please Enter book quantity: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    isbn = random.randint(10000, 99999)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": current_time,
        "bookLastUpdatedAt": current_time
    }
    all_books.append(new_book)
    save_all_books.save_all_books(all_books)
    print("Books Added Successully")
    return all_books
