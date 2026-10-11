import tkinter as tk
from tkinter import ttk, messagebox


class LibraryView:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("900x650")

        heading = ttk.Label(
            root,
            text="LIBRARY MANAGEMENT SYSTEM",
            font=("Arial", 18, "bold")
        )
        heading.pack(pady=12)

        form = ttk.LabelFrame(root, text="Book Details")
        form.pack(fill="x", padx=15, pady=8)

        self.book_id = tk.StringVar()
        self.title = tk.StringVar()
        self.author = tk.StringVar()
        self.quantity = tk.StringVar()
        self.borrower = tk.StringVar()
        self.issue_id = tk.StringVar()
        self.keyword = tk.StringVar()

        fields = [
            ("Book ID", self.book_id),
            ("Title", self.title),
            ("Author", self.author),
            ("Quantity", self.quantity),
            ("Borrower Name", self.borrower),
            ("Issue ID (for return)", self.issue_id),
            ("Search", self.keyword)
        ]

        for index, (label, variable) in enumerate(fields):
            row, col = divmod(index, 2)

            ttk.Label(form, text=label).grid(
                row=row, column=col * 2,
                padx=8, pady=7, sticky="w"
            )

            ttk.Entry(
                form, textvariable=variable, width=28
            ).grid(
                row=row, column=col * 2 + 1,
                padx=8, pady=7
            )

        self.add_button = ttk.Button(
            form, text="Add Book"
        )
        self.add_button.grid(
            row=4, column=0, padx=5, pady=10
        )

        self.issue_button = ttk.Button(
            form, text="Issue Book"
        )
        self.issue_button.grid(
            row=4, column=1, padx=5, pady=10
        )

        self.return_button = ttk.Button(
            form, text="Return Book"
        )
        self.return_button.grid(
            row=4, column=2, padx=5, pady=10
        )

        self.search_button = ttk.Button(
            form, text="Search"
        )
        self.search_button.grid(
            row=5, column=0, padx=5, pady=8
        )

        self.all_button = ttk.Button(
            form, text="View All Books"
        )
        self.all_button.grid(
            row=5, column=1, padx=5, pady=8
        )

        self.issued_button = ttk.Button(
            form, text="Issued Books"
        )
        self.issued_button.grid(
            row=5, column=2, padx=5, pady=8
        )

        self.tree = ttk.Treeview(
            root,
            columns=("ID", "Title", "Author", "Quantity"),
            show="headings",
            height=12
        )

        for column in ("ID", "Title", "Author", "Quantity"):
            self.tree.heading(column, text=column)

        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Title", width=260)
        self.tree.column("Author", width=220)
        self.tree.column("Quantity", width=100, anchor="center")

        self.tree.pack(
            fill="both", expand=True, padx=15, pady=10
        )

    def show_books(self, books):
        self.tree.delete(*self.tree.get_children())

        for book in books:
            self.tree.insert("", "end", values=book)

    def show_issued(self, issues):
        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = (
            "Issue ID", "Title", "Borrower", "Issue Date"
        )

        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=180)

        for issue in issues:
            self.tree.insert("", "end", values=issue)

    def reset_book_columns(self):
        self.tree["columns"] = (
            "ID", "Title", "Author", "Quantity"
        )

        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)

    def clear_book_fields(self):
        self.book_id.set("")
        self.title.set("")
        self.author.set("")
        self.quantity.set("")

    def info(self, message):
        messagebox.showinfo("Library System", message)

    def error(self, message):
        messagebox.showerror("Error", message)
