import json
from datetime import datetime

def restore_all_books():
    try:
        with open("all_books.json", "r") as fp:
            all_books = json.load(fp)

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for book in all_books:
            book.setdefault("bookAddedAt", current_time)
            book.setdefault("bookLastUpdatedAt", current_time)

        return all_books
    except FileNotFoundError:
        print("No saved books found.")
        return []