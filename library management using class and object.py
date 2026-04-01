books={}
issuebooks={}

class Library:
    def option(self):
        print("1. Add Book..")
        print("2. Issue Book..")
        print("3. Search Book..")
        print("4. Exit..")

    def addbook(self):
        bookname=input("Enter Name Of Book:- ")
        bookisbn=int(input("Enter ISBN Number:- "))
        books[bookisbn]=bookname

        print("Book added successful")

    def issuebook(self):
        userisbn=int(input("Enter ISBN Number: "))
        if userisbn in books:
            
            books.pop(userisbn)
            print("Book issue ")
        else:
            print("Book not found!")


        



l=Library()
option=0
while option<5:
    l.option()
    option=int(input("Enter option:- "))

    match option:
        case 1:
            l.addbook()
            print(books)
            
        case 2:
            l.issuebook()

