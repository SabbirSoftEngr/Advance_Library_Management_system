import save_all_books 
from datetime import datetime
def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")
    for book in all_books:
        if book['title'] == search_book:
            print("Leave input blank to skip updating a field.")

            new_title = input("Enter updated title: ").strip() or None
            if new_title:
                book['title'] = new_title

            new_author = input("Enter updated author: ").strip() or None
            if new_author:
                book['author'] = new_author

            new_year = input("Enter updated year: ").strip() or None
            if new_year:
                try:
                    book['year'] = int(new_year)
                except ValueError:
                    print("Invalid input for year. Skipping update.")

            new_price = input("Enter updated price: ").strip() or None
            if new_price:
                try:
                    book['price'] = int(new_price)
                except ValueError:
                    print("Invalid input for price. Skipping update.")

            new_quantity = input("Enter updated quantity: ").strip() or None
            if new_quantity:
                try:
                    book['quantity'] = int(new_quantity)
                except ValueError:
                    print("Invalid input for quantity. Skipping update.")

            print("Book updated successfully!")
            return all_books

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = new_title,
            book["author"] = new_author,
            book["year"] = new_year,
            book["price"] = new_price,
            book["quantity"] = new_quantity,
            book["bookLastUpdatedAt"] = book_last_updated_at

            save_all_books.save_all_books(all_books)
            print("Book Updated Successfully")
            return all_books
        
    print("Book not found!")
    return all_books
