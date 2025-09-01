# Book (name,author,price) initialize attribute

# Constructor

# is a special method that is automatically invoked when an object of the class is created
# Used for initialize instance variable.

# constructor special_name: __init__

class Book:

    def __init__(self,name,author,price):

        self.name = name
        
        self.author = author

        self.price = price

    def display_book(self):

        print(self.name,self.author,self.price)


book_instance1 = Book("goat life","benyamin",560)

book_instance1.display_book()