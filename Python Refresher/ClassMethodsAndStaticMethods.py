##
class ClassTest:
    ##Requires an instance of the class to exist for it to be called, an action that contains data or uses the data within the instance
    def instanceMethod(self):
        print(f"Called instanceMethod of {self}")

    ##Doesnt require an instance of the class, just the class itself used as "factories"
    @classmethod
    def classMethod(cls):
        print(f"Called classMethod of {cls}")
    
    ##Doesnt require the class for use and doesnt need an instance either. basically a function that lives inside the class but is not tied to it. put here for orginization
    @staticmethod
    def staticMethod():
        print("Called Static Method")


ClassTest.staticMethod()
ClassTest.classMethod()
test = ClassTest()
test.instanceMethod()

class Book:
    TYPES = ("hardcover", "paperback")
    def __init__(self, name, bookType, weight):
        self.name = name
        self.bookType = bookType
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.bookType}, weighing {self.weight}g>"
    ##Note Book and cls are the same and are interchangable, cls is the standard
    @classmethod
    def hardcover(cls, name, pageWeight):
        return Book(name, Book.TYPES[0], pageWeight + 100)
    @classmethod
    def paperback(cls, name, pageWeight):
        return cls(name, cls.TYPES[1], pageWeight)

## book = Book("Harry Potter", "hardcover", 1500) **Bad because the types of book is in the class
book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 800)
print(book)
print(light)
