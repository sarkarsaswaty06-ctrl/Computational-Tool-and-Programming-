class LibraryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        view.add_button.config(command=self.add_book)
        view.issue_button.config(command=self.issue_book)
        view.return_button.config(command=self.return_book)
        view.search_button.config(command=self.search_book)
        view.all_button.config(command=self.show_all_books)
        view.issued_button.config(command=self.show_issued_books)

        self.show_all_books()

    def add_book(self):
        try:
            book_id = int(self.view.book_id.get())
            title = self.view.title.get().strip()
            author = self.view.author.get().strip()
            quantity = int(self.view.quantity.get())

            if book_id <= 0 or quantity < 0:
                raise ValueError(
                    "Book ID must be positive and quantity non-negative."
                )

            if not title or not author:
                raise ValueError("Title and author are required.")

            self.model.add_book(
                book_id, title, author, quantity
            )

            self.view.info("Book added successfully.")
            self.view.clear_book_fields()
            self.show_all_books()

        except ValueError as error:
            self.view.error(str(error))
        except Exception as error:
            self.view.error(
                f"Unable to add book. Check whether the ID exists.\n{error}"
            )

    def issue_book(self):
        try:
            book_id = int(self.view.book_id.get())
            borrower = self.view.borrower.get().strip()

            if not borrower:
                raise ValueError("Enter the borrower's name.")

            self.model.issue_book(book_id, borrower)

            self.view.info("Book issued successfully.")
            self.show_all_books()

        except ValueError as error:
            self.view.error(str(error))
        except Exception as error:
            self.view.error(str(error))

    def return_book(self):
        try:
            issue_id = int(self.view.issue_id.get())

            self.model.return_book(issue_id)

            self.view.info("Book returned successfully.")
            self.show_all_books()

        except ValueError as error:
            self.view.error(str(error))
        except Exception as error:
            self.view.error(str(error))

    def search_book(self):
        keyword = self.view.keyword.get().strip()

        self.view.reset_book_columns()
        books = self.model.search_books(keyword)
        self.view.show_books(books)

        if not books:
            self.view.info("No matching books found.")

    def show_all_books(self):
        self.view.reset_book_columns()
        books = self.model.get_all_books()
        self.view.show_books(books)

    def show_issued_books(self):
        issues = self.model.get_issued_books()
        self.view.show_issued(issues)
