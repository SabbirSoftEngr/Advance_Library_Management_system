from datetime import datetime

def initialize_lend_records():
    return {}

def lend_book(books, lend_records, borrower_name, borrower_phone, book_title, return_date):
    if book_title in books:
        if books[book_title] > 0:
            try:
                due_date = datetime.strptime(return_date, "%Y-%m-%d")
                lend_records[borrower_phone] = {
                    "Name": borrower_name,
                    "Book Title": book_title,
                    "Due Date": due_date
                }
                books[book_title] -= 1
                print(f"\n[INFO] '{book_title}' has been lent to {borrower_name}.")
            except ValueError:
                print("\n[ERROR] Invalid date format. Please use YYYY-MM-DD.")
        else:
            print("\n[ERROR] Not enough copies available to lend.")
    else:
        print("\n[ERROR] Book not found in the library.")

def return_book(books, lend_records, borrower_phone):
    if borrower_phone in lend_records:
        book_title = lend_records[borrower_phone]["Book Title"]
        books[book_title] += 1
        del lend_records[borrower_phone]
        print(f"\n[INFO] '{book_title}' has been successfully returned.")
    else:
        print("\n[ERROR] No lending record found for this phone number.")

def view_lend_records(lend_records):
    if not lend_records:
        print("\n[INFO] No books are currently lent out.")
    else:
        print("\n[INFO] Lending Records:")
        for phone, details in lend_records.items():
            due_date = details["Due Date"].strftime("%Y-%m-%d")
            print(f"Phone: {phone}, Name: {details['Name']}, Book: {details['Book Title']}, Due Date: {due_date}")
