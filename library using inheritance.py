class Library():
    name=""
    booksquantity=0

    def lname(self):
        print(f"Name of Library: {self.name}")
    def content(self):
        print(f"{self.name} total books: {self.booksquantity}")
    
    def types(self,t):
        print(f"{self.name} type {t} library")

class Book(Library):
    bname=""

    def btype(self,type):
        print(f"Type of book: {type}" )

    def read(self):
        print(f"{self.bname} ready by {s.sname}")
    


class Student(Book):
    sname=""
    sage=0
    scollege=""

    def take(self):
        print(f"{self.sname}Take book")

    def studentinfo(self):
        print(f"Name of Student: {self.sname}")
        print(f"Age of Student: {self.sage}")
        print(f"College of Student: {self.scollege}")



s=Student()
s.name="topper"
s.booksquantity=50
s.bname="Shutter Island"
s.sname="prashil"
s.sage=18
s.scollege="Takshshila"
s.lname()
s.content()
s.types("digital")
s.btype("Mystery")
s.read()
s.studentinfo()
