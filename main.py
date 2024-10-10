from insides.library import Library

library = Library()

while True:
    print("\nOptions:"
          "\n[1] Add a new book"
          "\n[2] Remove old books"
          "\n[3] Show all books"
          "\n[9] Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = int(input("Enter year of publication: "))
        genre = input("Enter genre: ")
        library.add_book(title, author, year, genre)
    
    elif choice == "2":
        break

    elif choice == "3":
        library.show_books()

    elif choice == "9":
        print("Exiting the program.")
        break

    else:
        print("ERROR")