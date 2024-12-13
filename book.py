import restore_books_file
import add_books
from view_all_books import view_all_books
from save_all_books import save_all_books
from update_book_file import update_books
from delete_book_file import delete_books
from main_library import initialize_books
from main_library import view_books
from lend_return import initialize_lend_records, lend_book, return_book, view_lend_records
all_books = []
all_books = restore_books_file.restore_all_books()
lend_record_books = []

def main_menu():
    books = initialize_books()
    lend_records = initialize_lend_records()

    while True:
        print("\nWelcome to Library Management System")
        print("0. Exit")
        print("1. View All Books from library")
        print("2. Lend a Book from library")
        print("3. Return a Book to library")
        print("4. View Lending Records")
        print("5. Add Books")
        print("6. View all added Books")
        print("7. Update a book")
        print("8. Delete/Remove a Books")

        menu = input("Select any number: ").strip()

        if menu == "0":
            save_all_books(all_books)
            print("Thanks for Using Library Management System")
            break
        elif menu == "1":
            view_books(books)
        elif menu == "2":
            borrower_name = input("Enter borrower's name: ").strip()
            borrower_phone = input("Enter borrower's phone number: ").strip()
            book_title = input("Enter book title: ").strip()
            return_date = input("Enter return due date (YYYY-MM-DD): ").strip()
            lend_book(books, lend_records, borrower_name, borrower_phone, book_title, return_date)
        elif menu == "3":
            borrower_phone = input("Enter borrower's phone number: ").strip()
            return_book(books, lend_records, borrower_phone)
        elif menu == "4":
            view_lend_records(lend_records)
        elif menu == "5":
            add_books.add_book(all_books)
        elif menu == "6":
            view_all_books(all_books)
        elif menu == "7":
            update_books(all_books)
        elif menu == "8":
            delete_books(all_books)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
