from datetime import datetime, timedelta
import pickle

from insides.book import Book
from insides.logins import Logins

class Library:
    def __init__(self):
        self.books = []
        self.rented_books = {}

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
            ("The Odyssey 2", "Homer", 800, "Epic Poetry"),
            ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Philosophical Fiction"),
        ]
        
# [1] Add a new book
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

# [2] Remove a book
    # (1) Delete by name:
    def remove_title_books(self, book_title) -> None:
        self.books = [book for book in self.books if book.pavadinimas != book_title]
        print(f"Removed {book_title} book.")

    # (2) Delete books older than year:
    def remove_old_books(self, year_limit: int) -> None:
        before_count = len(self.books)
        # Correctly access the year attribute
        self.books = [book for book in self.books if book.isleidimo_metai >= year_limit]
        after_count = len(self.books)
        print(f"Removed {before_count - after_count} old books.")

# [3] Show all books
    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return
        
        for book in self.books:
            print("-" * 70)
            print(book)

# [4] Rent a book
    def rent_book(self, name: str, book_title: str) -> None:
        rented_book = [book for book in self.books if book.pavadinimas == book_title]

        today = datetime.now()

        # Check if user has overdue books
        if name in self.rented_books:
            for _, expiration in self.rented_books[name].items():
                expiration_date = datetime.strptime(expiration, "%m-%d")
                if expiration_date < today:
                    print(f"{name} has overdue books and cannot rent more.")
                    return

        # Check if user has reached the maximum amount of rentable books
        if name in self.rented_books and len(self.rented_books[name]) >= 3:
            print(f"Error: {name} has already rented the maximum of 3 books.")
            return

        expiration_date = (today + timedelta(days=7)).strftime("%m-%d")  # Create rental deadline

        if rented_book:
            rented_book = rented_book[0]
            self.books.remove(rented_book)

            if name in self.rented_books:
                self.rented_books[name][rented_book.pavadinimas] = expiration_date
            else:
                self.rented_books[name] = {rented_book.pavadinimas: expiration_date}

            print(f"{name} rented '{rented_book.pavadinimas}' book, return by {expiration_date}")
        else:
            print("No book found.")

# [5] Show all rented books
    def show_rented_books(self) -> None:
        if not self.rented_books:
            print("No rented books")
            return # To exit

        print("Rented books:")
        for name, rented_books in self.rented_books.items():
            print("-" * 50)
            print(f"{name} has rented the following books: ")
            for book_title, expiration_date in rented_books.items():
                print(f"'{book_title}' (Return by: {expiration_date})")

# [6] Search
    # (1) Search by name: 
    def search_by_title(self, name) -> None:
        for book_name in self.books:
            if name == book_name.pavadinimas:
                print(f"Book '{name}' is in the library.")
                return
            
        print("Sorry we don't have this book")
        
    # "(2) Search by author: "
    def search_by_author(self, author) -> None:
        found = []

        for book_author in self.books:
            if author == book_author.autorius:
                found.append(book_author.pavadinimas)

        if len(found) == 0:
            print("Sorry we don't have book of this author")
            return
        
        print(f"{author} wrote these books: {found}")

# [7] Show all overdue books
    def show_overdue_books(self) -> None:
        current_date = datetime.now()

        overdue_books_found = False  # To check if we find any overdue books
        for name, books in self.rented_books.items():
            overdue_books = []
            
            for book_title, expiration_date in books.items():
                expiration_datetime = datetime.strptime(expiration_date, "%m-%d").replace(year = current_date.year)
                
                if expiration_datetime < current_date:
                    overdue_books.append(book_title)

            if overdue_books:
                overdue_books_found = True
                print(f"{name} has overdue the following books: {', '.join(overdue_books)}")
        
        if not overdue_books_found:
            print("No overdue books at the moment.")

    # [8] Load
    def load_data(self, filename="library_data.pkl") -> None:
        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
                self.books = data['books']
                self.rented_books = data['rented_books']
            
            print(f"Library data loaded from {filename}.")
        except FileNotFoundError:
            print(f"No saved data found in {filename}.")

    # [9] Save
    def save_data(self, filename="library_data.pkl") -> None:
        data = {
            'books': self.books,
            'rented_books': self.rented_books
        }
        
        with open(filename, "wb") as file:
            pickle.dump(data, file)
        
        print(f"Library data saved to {filename}.")