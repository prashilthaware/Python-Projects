print("find the area of:-")
print("1.Circle")
print("2.Square")
print("3.Triangle")
print("4.Rectangle")
opt=int(input("Enter option:- "))

match opt:
    case 1:
        radius=int(input("Enter radius:"))
        value=3.14*radius*radius
        print(f"The area of circle is: {value}")

    case 2:
        side=int(input("Enter side:"))
        value1=side*side
        print(f"The area of Square is: {value1}")

    case 3:
        base=int(input("Enter base:"))
        hight=int(input("Enter hight:"))
        value3=base*hight/2
        print(f"The area of Triangle is: {value3}")

    case 4:
        length=int(input("Enter length:"))
        width=int(input("Enter bredth:"))
        value4=length*width
        print(f"The area of Rectangle is: {value4}")