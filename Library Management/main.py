import json

class Library:
    def __init__(self, file_path="library_management.txt"):
        self.file_path = file_path
        self.books = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.books, file, indent=2)

    def create_book(self, title, author, genre):
        book_id = len(self.books) + 1
        book = {
            'id': book_id,
            'title': title,
            'author': author,
            'genre': genre
        }
        self.books.append(book)
        self.save_data()
        return f"Book added successfully with ID {book_id}."

    def read_books(self):
        if not self.books:
            return "No books in the library."
        else:
            return self.books

    def update_book(self, book_id, new_title=None, new_author=None, new_genre=None):
        for book in self.books:
            if book['id'] == book_id:
                if new_title:
                    book['title'] = new_title
                if new_author:
                    book['author'] = new_author
                if new_genre:
                    book['genre'] = new_genre
                self.save_data()
                return f"Book with ID {book_id} updated successfully."
        return f"Book with ID {book_id} not found."

    def delete_book(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                self.save_data()
                return f"Book with ID {book_id} deleted successfully."
        return f"Book with ID {book_id} not found."

def display_menu():
    print("Library Management System")
    print("1. Add a book")
    print("2. View all books")
    print("3. Update a book")
    print("4. Delete a book")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def main():
    library = Library()

    while True:
        choice = display_menu()

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            print(library.create_book(title, author, genre))

        elif choice == '2':
            books = library.read_books()
            if isinstance(books, list):
                for book in books:
                    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
            else:
                print(books)

        elif choice == '3':
            book_id = int(input("Enter the ID of the book you want to update: "))
            new_title = input("Enter the new title (press Enter to keep the existing title): ")
            new_author = input("Enter the new author (press Enter to keep the existing author): ")
            new_genre = input("Enter the new genre (press Enter to keep the existing genre): ")
            print(library.update_book(book_id, new_title, new_author, new_genre))

        elif choice == '4':
            book_id = int(input("Enter the ID of the book you want to delete: "))
            print(library.delete_book(book_id))

        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
