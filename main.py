# TO do
from insides.library import Library
from insides.logins import Logins


library = Library()
logins = Logins()

while True:
    print("\nOptions:")
    print("[1] Log in")
    print("[2] Register")
    print("[3] Load")
    print("[4] Save")
    print("[5] Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
    
        login_status = logins.log_in(username, password)

        if login_status == "admin":
            print("You are admin")

            while True:
                print("\nOptions:")
                print("[1] Add a new book")
                print("[2] Remove a book")
                print("[3] Show all books")
                print("[5] Show all rented books")
                print("[6] Search")
                print("[7] Show all overdue books")
                print("[10] Log out")

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
                    print("(1) Delete by name: "
                        "(2) Delete books older than year: ")
                    
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

                elif choice == '5':
                    library.show_rented_books()

                elif choice == '6':
                    print("(1) Search by name: "
                        "(2) Search by author: ")
                    
                    choice = input("Choose an option: ")

                    if choice == "1":
                        library.show_books()
                        book_title = input("Enter book title: ")
                        library.search_by_title(book_title)

                    elif choice == "2":
                        library.show_books()
                        book_author = input("Enter book author: ")
                        library.search_by_author(book_author)

                    else:
                        print("Invalid option, please try again.")

                elif choice == '7':
                    library.show_overdue_books()

                elif choice == '10':
                    print("Logging out.")
                    break

                else:
                    print("Invalid option, please try again.")

        if login_status == "user":
            print("You are user")

            while True:
                print("\nOptions:")
                print("[3] Show all books")
                print("[4] Rent a book")
                print("[6] Search")
                print("[10] Log out")

                choice = input("Choose an option: ")

                if choice == '3':
                    library.show_books()

                elif choice == '4':
                    name = input("Enter your name for rent: ")
                    library.show_books()
                    book_title = input("Enter book name for rent: ")
                    library.rent_book(name, book_title)

                elif choice == '6':
                    print("(1) Search by name: "
                        "(2) Search by author: ")
                    
                    choice = input("Choose an option: ")

                    if choice == "1":
                        library.show_books()
                        book_title = input("Enter book title: ")
                        library.search_by_title(book_title)

                    elif choice == "2":
                        library.show_books()
                        book_author = input("Enter book author: ")
                        library.search_by_author(book_author)

                    else:
                        print("Invalid option, please try again.")

                elif choice == '10':
                    print("Logging out")
                    break

                else:
                    print("Invalid option, please try again.")

        if login_status == "failed":
            print("Login failed. Please try again.")
            continue

    # while True:
    #     print("\nOptions:")
    #     print("[1] Add a new book")
    #     print("[2] Remove a book")
    #     print("[3] Show all books")
    #     print("[4] Rent a book")
    #     print("[5] Show all rented books")
    #     print("[6] Search")
    #     print("[7] Show all overdue books")
    #     print("[8] Load")
    #     print("[9] Save")
    #     print("[10] Exit")

    #     choice = input("Choose an option: ")

    #     if choice == '1':
    #         title = input("Enter book title (type 'def' to add preset books): ")
    #         if title.lower() == "def":
    #             # Added preset of books
    #             library.add_book(title)
    #         else:
    #             author = input("Enter author: ")
    #             year = int(input("Enter year of publication: "))
    #             genre = input("Enter genre: ")
    #             library.add_book(title, author, year, genre)
            
    #     elif choice == '2':
    #         print("(1) Delete by name: "
    #             "(2) Delete books older than year: ")
            
    #         choice = input("Choose an option: ")

    #         if choice == "1":
    #             library.show_books()
    #             book_title = input("Enter book title: ")
    #             library.remove_title_books(book_title)

    #         elif choice == "2":
    #             library.show_books()
    #             year_limit = int(input("Enter year limit for removal: "))
    #             library.remove_old_books(year_limit)
    #         else:
    #             print("Invalid option, please try again.")

    #     elif choice == '3':
    #         library.show_books()

    #     elif choice == '4':
    #         name = input("Enter your name for rent: ")
    #         library.show_books()
    #         book_title = input("Enter book name for rent: ")
    #         library.rent_book(name, book_title)

    #     elif choice == '5':
    #         library.show_rented_books()

    #     elif choice == '6':
    #         print("(1) Search by name: "
    #             "(2) Search by author: ")
            
    #         choice = input("Choose an option: ")

    #         if choice == "1":
    #             library.show_books()
    #             book_title = input("Enter book title: ")
    #             library.search_by_title(book_title)

    #         elif choice == "2":
    #             library.show_books()
    #             book_author = input("Enter book author: ")
    #             library.search_by_author(book_author)

    #         else:
    #             print("Invalid option, please try again.")

    #     elif choice == '7':
    #         library.show_overdue_books()

    #     elif choice == '8':
    #         library.load_data()

    #     elif choice == '9':
    #         library.save_data()
        
    #     elif choice == '10':
    #         print("Exiting program")
    #         break

    #     else:
    #         print("Invalid option, please try again.")