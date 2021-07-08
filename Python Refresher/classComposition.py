#!class BookShelf:
    #!def __init__(self, quantity):
        #!self.quantity = quantity

    #!def __str__(self):
        #!return f"BookShelf with {self.quantity} books."


#!shelf = BookShelf(300)

##Requires the quanity to be present (inherited from the BookShelf) the Book is a Bookshelf and more. which makes no sense. Technically, Book is inheriting the BookShelf class, and you dont need ANYTHING from BookShelf
#!class Book(BookShelf):
    #!def __init__(self, name, quantity):
        #!#!self.name = name

#!book = Book("Harry Potter", 120)
#!print(book)  # What?

##Instead, make a BookShelf that is composed of books

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

class Book:
    def __init__(self, name):
        self.name = name

book =  Book("Harry Potter")
book2 = Book("Python")
shelf = BookShelf(book, book2)

print(shelf)

##Composistion is when a class is comprised of many other classes