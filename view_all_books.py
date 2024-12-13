import json

def view_all_books(all_books):
    try:
        with open("all_books.json", "r") as fp:
            all_books = json.load(fp)

        if not all_books:
            print("No books to display.")
            return

        for book in all_books:
            print(f"Title: {book.get('title', 'N/A')} | "
                  f"Author: {book.get('author', 'N/A')} | "
                  f"ISBN: {book.get('isbn', 'N/A')} | "
                  f"Year: {book.get('year', 'N/A')} | "
                  f"Price: {book.get('price', 'N/A')} | "
                  f"Quantity: {book.get('quantity', 'N/A')} | "
                  f"Book Added At: {book.get('bookAddedAt', 'N/A')} | "
                  f"Book Last Updated At: {book.get('bookLastUpdatedAt', 'N/A')}")
    except FileNotFoundError:
        print("The file 'all_books.json' does not exist.")
    except json.JSONDecodeError:
        print("Error decoding the JSON file.")