class LibraryBook:
    def __init__(self, title, is_available=True):
        self.title = title
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print("Kitob olindi")
        else:
            print("Band")

    def return_book(self):
        self.is_available = True
        print("Kitob qaytarildi")


# Obyekt
book = LibraryBook("Python")
book.borrow()
book.borrow()
book.return_book()
