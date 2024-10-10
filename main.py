# kokmetaras
from insides.library import Library


library = Library()
    
while True:
    print("\nOptions:")
    print("[1] Add a new book")
    print("[2] Remove a book")
    print("[3] Show all books")
    print("[9] Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        title = input("Enter book title (type 'def' to add preset books): ")
        if title.lower() == "def":
            # Added preset of books
            library.add_book(title)
        else:
            author = input("Enter author: ")
            year = int(input("Enter year of publication: "))
            genre = input("Enter genre: ")
            library.add_book(title, author, year, genre)
        
    elif choice == '2':
        print("[1] Delete by name: "
              "[2] Delete books older than year: ")
        choice = input("Choose an option: ")
        if choice == "1":
            library.show_books()
            book_title = input("Enter book title: ")
            library.remove_title_books(book_title)

        elif choice == "2":
            library.show_books()
            year_limit = int(input("Enter year limit for removal: "))
            library.remove_old_books(year_limit)
        else:
            print("Invalid option, please try again.")

    elif choice == '3':
        library.show_books()
        
    elif choice == '9':
        print("Exiting the program.")
        break

    else:
        print("Invalid option, please try again.")