# book.py
class Book:
    def __init__(self, pavadinimas: str, autorius: str, isleidimo_metai: int, zanras: str) -> None:
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.isleidimo_metai = isleidimo_metai  # Use the correct attribute name
        self.zanras = zanras

    def __str__(self):
        return f"{self.pavadinimas} by {self.autorius} ({self.isleidimo_metai}) - Genre: {self.zanras}"
