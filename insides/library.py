# Kuriamas sarasas asf
class Library:
    def __init__(self, pavadinimas: str, autorius: str, isleidimo_metai: float, zanras: str) -> None:
        self.pavadinimas = pavadinimas
        self.autorius = autorius
        self.isleidimo_metai = isleidimo_metai
        self.zanras = zanras


class MyBooks:
    def __init__(self) -> None:
        self.library = []
