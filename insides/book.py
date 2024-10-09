# Kuriamas saras
class Library:
    def __init__(self, pavadinimas: str, autorius: str, isleidimo_metai: float, zanras: str) -> None:
        self.pavadinimas, self.autorius, self.isleidimo_metai, self.zanras = pavadinimas, autorius, isleidimo_metai, zanras
    

# Kuriama kintamasis
class MyBooks:
    def __init__(self) -> None:
        self.library = []

    def add_book(self):
        while True:
            add_exit = input("add book (a) or exit (e)")
            if add_exit.islower == "e":
                break
            pavadinimas = input("Iveskite autoriu: ")
            autorius = input("Iveskite pavadinima: ")
            isleidimo_metai = float(input("Iveskite isleidimo metus: "))
            zanras = input("Iveskite zanra: ")

            knyga = Library(pavadinimas, autorius, isleidimo_metai, zanras)
            self.library.append(knyga)
        
    def display_book(self):
        for book in self.library:
            print(f"{book.pavadinimas} by {book.autorius}, {book.isleidimo_metai}, {book.zanras}")

my_books = MyBooks()
my_books.add_book()

my_books.display_book()
        
# Tests

