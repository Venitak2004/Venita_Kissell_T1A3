def main():
    
    books = []
    choice = 0

    while choice != 4:
        print("Library manager")
        print("1. Add a book")
        print("2. Find a book")
        print("3. Show all books")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4")
            continue

        if choice == 1:
            print("Adding book")
            title = input("Enter title: ")
            gender = input(" enter book gender: ")
            author = input("Enter author: ")
            books.append([title, gender, author])

        elif choice == 2:
            print("Finding a book")
            search_word = input("Enter search word: ")
            for book in books:
                if search_word in book[0] or search_word in book[1] or search_word in book[2]:
                    print(book)
        
        elif choice == 3:
            print("showing all books")
            for book in books:
                print(book)
        
        elif choice == 4:
            print("exiting program")
            break

        else:
            print("Invalid choice. Please enter a number bewtween 1 and 4.")

    print("program terminated")

if __name__ == "__main__":
    main()