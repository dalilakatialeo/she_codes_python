class Book:
    #attributes, title, author, size, pages, colour, pictures, thickness
    #methods - turning a page, closing, opening

    def __init__(self, title, author, pages, current_page): #init always takes 3 attributes, but self is never used again or referred to when calling 
        #assisgnment to object attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1 #creating an attribute inside the intialiser - it assigns 1 by default
        #initialisers do not return, other methods can return

    def bookmark_page(self, page):
        if page < self.pages:
            self.bookmark = page

    def turn_page(self):
        if self.current_page == self.pages:
            self.current_page = 1
        else:
            self.current_page += 1


    def page_back (self):
        self.current_page -= 1

    def go_to_page(self, page):
        if page < self.pages:
            self.current_page = page

    #double underscore method is a special kind, computer knows what this is even if we dont define it, but we want to make sure it does what is expected, so if we need it, we want to define it
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    #create a method turn back the page

my_book = Book("A great book", "me", 100, 98)
# my_book.go_to_page(7)
# print(my_book.current_page)
# print(my_book) #prints everything that is printable
# # print(my_book.__str__()) #prints one specific method 
# # my_book.bookmark_page(12)
# print(my_book.bookmark)
my_book.go_to_page(99)
print(my_book.current_page) #print 100
my_book.turn_page() #method #page 11
print(my_book.current_page)
my_book.turn_page() #page 12
print(my_book.current_page)
my_book.turn_page() #page 13
print(my_book.current_page)
my_book.turn_page() #page 14
# my_book.bookmark_page() #page 15
# my_book.page_back() #page 14
# my_book.bookmark_page() #page 15
# print(my_book.bookmark) #page 14


#create function to check in page within book (call function within class) - challenge