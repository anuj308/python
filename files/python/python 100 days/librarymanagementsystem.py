# library class has atleat two variable no_of_books(int),books(list) method - print books , add books by that no of bools sholud be increasing , 
# get the no of book and len no of books is not equal that you have added show an error message that program has error

class Library:
    def __init__(self):
        self.books=[]
        self.no_of_book=0
    def addbook(self,book_name):
        self.book_name=book_name
        self.books.append(self.book_name)
        self.no_of_book+=1
    def showbooks(self):
        print(f"no of books are in libray are {self.books}")
    def noofbook(self):
        lenbook=len(self.books)
        print(f"{self.no_of_book}")
        if lenbook!=self.no_of_book:
            print("there is some error in program")
l1=Library()
l1.addbook("Bharat")
l1.addbook("India | The next superpower")
l1.showbooks()
l1.noofbook()

