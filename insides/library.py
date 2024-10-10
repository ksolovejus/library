from insides.book import Book

class Library:
    def __init__(self):
        self.books = []

        # Preset of books 
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

    def add_book(self, title:str, author: str, year: int, genre: str) -> None:
        new_book = Book(title, author, year, genre)
        self.books.append(new_book)
        print(f"Added: {new_book}")

    def show_books(self):
        if not self.books:
            print("No books in the library")
        for book in self.books:
            print("*" * 70)
            print(book)