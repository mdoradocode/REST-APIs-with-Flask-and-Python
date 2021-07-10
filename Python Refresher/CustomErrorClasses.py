##Need to inherit from an exception class or a value Error class to raise it
class tooManyPagesError(ValueError):
    pass

class Book:
    def __init__(self, name: str, pageCount: int):
        self.name = name
        self.pageCount = pageCount
        self.pagesRead = 0
    
    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.pagesRead} pages out of {self.pageCount}>"
        )
    
    def read(self, pages: int):
        if self.pagesRead + pages > self.pageCount:
            raise tooManyPagesError
            (
                print("You tried to read more pages then are allowed in the book!")
            )
        self.pagesRead += pages
        print(f"You have now read {self.pagesRead} pages out of {self.pageCount}")

book1 = Book("Harry Potter",100)
book1.read(50)
book1.read (75)