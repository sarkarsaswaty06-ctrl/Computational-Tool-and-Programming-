import sqlite3


class LibraryModel:
    def __init__(self, db_name="library.db"):
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        with self.connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    quantity INTEGER NOT NULL CHECK(quantity >= 0)
                )
            """)

            conn.execute("""
                CREATE TABLE IF NOT EXISTS issues (
                    issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER NOT NULL,
                    borrower TEXT NOT NULL,
                    issue_date TEXT NOT NULL DEFAULT
                        (date('now', 'localtime')),
                    return_date TEXT,
                    FOREIGN KEY(book_id) REFERENCES books(book_id)
                )
            """)

    def add_book(self, book_id, title, author, quantity):
        with self.connect() as conn:
            conn.execute(
                """INSERT INTO books
                   (book_id, title, author, quantity)
                   VALUES (?, ?, ?, ?)""",
                (book_id, title, author, quantity)
            )

    def get_all_books(self):
        with self.connect() as conn:
            return conn.execute("""
                SELECT book_id, title, author, quantity
                FROM books ORDER BY book_id
            """).fetchall()

    def search_books(self, keyword):
        with self.connect() as conn:
            pattern = f"%{keyword}%"
            return conn.execute("""
                SELECT book_id, title, author, quantity
                FROM books
                WHERE CAST(book_id AS TEXT) LIKE ?
                   OR title LIKE ?
                   OR author LIKE ?
                ORDER BY book_id
            """, (pattern, pattern, pattern)).fetchall()

    def issue_book(self, book_id, borrower):
        with self.connect() as conn:
            book = conn.execute("""
                SELECT quantity FROM books WHERE book_id = ?
            """, (book_id,)).fetchone()

            if book is None:
                raise ValueError("Book ID not found.")

            if book[0] <= 0:
                raise ValueError("No copies of this book are available.")

            conn.execute("""
                INSERT INTO issues (book_id, borrower)
                VALUES (?, ?)
            """, (book_id, borrower))

            conn.execute("""
                UPDATE books SET quantity = quantity - 1
                WHERE book_id = ?
            """, (book_id,))

    def return_book(self, issue_id):
        with self.connect() as conn:
            issue = conn.execute("""
                SELECT book_id FROM issues
                WHERE issue_id = ? AND return_date IS NULL
            """, (issue_id,)).fetchone()

            if issue is None:
                raise ValueError(
                    "Active issue record not found."
                )

            conn.execute("""
                UPDATE issues
                SET return_date = date('now', 'localtime')
                WHERE issue_id = ?
            """, (issue_id,))

            conn.execute("""
                UPDATE books SET quantity = quantity + 1
                WHERE book_id = ?
            """, (issue[0],))

    def get_issued_books(self):
        with self.connect() as conn:
            return conn.execute("""
                SELECT i.issue_id, b.title, i.borrower,
                       i.issue_date
                FROM issues i
                JOIN books b ON i.book_id = b.book_id
                WHERE i.return_date IS NULL
                ORDER BY i.issue_id
            """).fetchall()
