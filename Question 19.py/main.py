import tkinter as tk
from model import LibraryModel
from view import LibraryView
from controller import LibraryController


def main():
    root = tk.Tk()

    model = LibraryModel()
    view = LibraryView(root)
    LibraryController(model, view)

    root.mainloop()


if __name__ == "__main__":
    main()
