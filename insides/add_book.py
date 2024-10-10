from library import Library, MyBooks

class AddBook:
    def __init__(self, book_collection):
        self.book_collection = book_collection

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

    def add_book(self):
        while True:
            pavadinimas = input("Iveskite pavadinima: ")
            if pavadinimas == "def":
                for title, author, year, genre in self.preset_books:
                    knyga = Library(title, author, year, genre)
                    self.book_collection.library.append(knyga)
                print("Default book list added!")
                break

            autorius = input("Iveskite autoriu: ")
            isleidimo_metai = float(input("Iveskite isleidimo metus: "))
            zanras = input("Iveskite zanra: ")

            # Create a new Library object and add to the book collection
            knyga = Library(pavadinimas, autorius, isleidimo_metai, zanras)
            self.book_collection.library.append(knyga)

            add_exit = input("add book (a) or exit (e): ")
            if add_exit.lower() == "e":
                break

    def display_books(self):
        i = 1
        for book in self.book_collection.library:
            print("-" * 70)
            print(f"{i}. {book.pavadinimas} by {book.autorius}, {book.isleidimo_metai}, {book.zanras}")
            i += 1


my_books = MyBooks()

book_adder = AddBook(my_books)
book_adder.add_book()

book_adder.display_books()
