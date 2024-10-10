from library import Library, MyBooks

class AddBook:
    def __init__(self, book_collection):
        self.book_collection = book_collection

    def add_book(self):
        while True:
            pavadinimas = input("Iveskite pavadinima: ")
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
        for book in self.book_collection.library:
            print(f"{book.pavadinimas} by {book.autorius}, {book.isleidimo_metai}, {book.zanras}")


my_books = MyBooks()

book_adder = AddBook(my_books)
book_adder.add_book()

book_adder.display_books()
