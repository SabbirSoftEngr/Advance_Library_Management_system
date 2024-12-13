def initialize_books():
    return {
        "Harry Potter": 4,
        "The Alchemist": 5,
        "Sherlock Holmes": 3
    }

def view_books(books):
    print("\n[INFO] Library Inventory:")
    for book, qty in books.items():
        print(f"{book}: {qty} copies")
