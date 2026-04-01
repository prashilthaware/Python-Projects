class Shapes:
    def shapelist(self):
        print("find the area of:-")
        print("1.Circle")
        print("2.Square")
        print("3.Triangle")
        print("4.Rectangle")
        print("5.Exit")

    def carea(self):
        radius=int(input("Enter radius:"))
        value=3.14*radius*radius
        print(f"The area of circle is: {value}")

    def sarea(self):
        side=int(input("Enter side:"))
        value1=side*side
        print(f"The area of Square is: {value1}")

    def tarea(self):
        base=int(input("Enter base:"))
        hight=int(input("Enter hight:"))
        value3=base*hight/2
        print(f"The area of Triangle is: {value3}")
    
    def rarea(self):
        length=int(input("Enter length:"))
        width=int(input("Enter bredth:"))
        value4=length*width
        print(f"The area of Rectangle is: {value4}")


s=Shapes()
option=0
while option<=5:
    s.shapelist()
    option=int(input("Enter option:- "))
    
    match option:
        case 1:
            s.carea()
        case 2:
            s.sarea()
        case 3:
            s.tarea()
        case 4:
            s.rarea()
        case 5:
            print("Exit!!!")





