# Library Management System using Inheritance and Polymorphism

# Base class
class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.is_issued = False

    def issue(self):
        if not self.is_issued:
            self.is_issued = True
            print(self.title, "has been issued.")
        else:
            print(self.title, "is already issued.")

    def return_item(self):
        if self.is_issued:
            self.is_issued = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print("ID:", self.item_id)
        print("Title:", self.title)
        print("Status:", status)


# Derived class: Book
class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    # Polymorphic method
    def display(self):
        super().display()
        print("Type: Book")
        print("Author:", self.author)


# Derived class: Magazine
class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number):
        super().__init__(item_id, title)
        self.issue_number = issue_number

    # Polymorphic method
    def display(self):
        super().display()
        print("Type: Magazine")
        print("Issue Number:", self.issue_number)


# Derived class: Journal
class Journal(LibraryItem):
    def __init__(self, item_id, title, volume):
        super().__init__(item_id, title)
        self.volume = volume

    # Polymorphic method
    def display(self):
        super().display()
        print("Type: Journal")
        print("Volume:", self.volume)


# Creating library items
items = [
    Book(101, "Python Programming", "John Smith"),
    Magazine(102, "Science Today", 25),
    Journal(103, "Computer Science Research", 12)
]

# Display all items
print("----- Library Items -----")
for item in items:
    item.display()
    print()

# Issue items
print("----- Issue Operations -----")
items[0].issue()
items[1].issue()

# Try issuing the same book again
items[0].issue()

# Return an item
print("\n----- Return Operations -----")
items[0].return_item()

# Try returning the same book again
items[0].return_item()

# Display updated status
print("\n----- Updated Library Status -----")
for item in items:
    item.display()
    print()
