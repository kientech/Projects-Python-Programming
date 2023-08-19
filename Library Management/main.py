import pandas as pd

class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = pd.DataFrame(columns=["Title", "Author", "Genre"])

    def add_book(self, title, author, genre):
        new_book = pd.DataFrame([[title, author, genre]], columns=["Title", "Author", "Genre"])
        self.books = self.books._append(new_book, ignore_index=True)

    def delete_book(self, title):
        self.books = self.books[self.books["Title"] != title].reset_index(drop=True)

    def search_book(self, title):
        result = self.books[self.books["Title"] == title]
        if len(result) > 0:
            return result
        else:
            return None

    def display_books(self):
        print(self.books)

    def save_to_file(self):
        self.books.to_excel(self.filename, index=False)

def main():
    library = Library("library.xlsx")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Save to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            library.add_book(title, author, genre)
            print("Book added to library.")
        elif choice == "2":
            title = input("Enter book title to delete: ")
            library.delete_book(title)
            print("Book deleted from library.")
        elif choice == "3":
            title = input("Enter book title to search: ")
            result = library.search_book(title)
            if result is not None:
                print(result)
            else:
                print("Book not found in library.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            library.save_to_file()
            print("Library saved to file.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
