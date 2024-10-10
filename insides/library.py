# library.py

from insides.book import Book

class Library:
    def __init__(self):
        self.books = []
        self.preset_books = [
            ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"),
            ("1984", "George Orwell", 1949, "Dystopian"),
            ("To Kill a Mockingbird", "Harper Lee", 1960, "Classic"),
            ("Moby Dick", "Herman Melville", 1851, "Adventure"),
            ("Pride and Prejudice", "Jane Austen", 1813, "Romance"),
            ("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction"),
            ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy"),
            ("War and Peace", "Leo Tolstoy", 1869, "Historical Fiction"),
            ("The Odyssey", "Homer", -800, "Epic Poetry"),
            ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Philosophical Fiction"),
        ]

    def add_book(self, title: str, author: str = None, year: int = None, genre: str = None) -> None: # added "= None" so program don't request author, year, genre in case of preset use
        if title.lower() == "def":
            for preset in self.preset_books:
                new_book = Book(*preset)  # Unpack the preset tuple
                self.books.append(new_book)
                print(f"Added: {new_book}")
        else:
            if author and year and genre:
                new_book = Book(title, author, year, genre)
                self.books.append(new_book)
                print(f"Added: {new_book}")
            else:
                print("Please provide author, year, and genre for the new book.")

    def remove_old_books(self, year_limit: int) -> None:
        before_count = len(self.books)
        # Correctly access the year attribute
        self.books = [book for book in self.books if book.isleidimo_metai >= year_limit]
        after_count = len(self.books)
        print(f"Removed {before_count - after_count} old books.")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)
