print("Temperature Converter")
tem=int(input("Enter Temperature:"))
print("1. celsius to fahrenheit")
print("2. fahrenheit to celsius")
print("3. celsius to kelvin")
print("4. kelvin to celsius")
opt=int(input("Enter option: "))

match opt:
    case 1:
        tem=(9/5)+32
        print(f"Temperature in Celsius to Fahrenheit {tem}")
    case 2:
        tem=(tem-32)*(5/9)
        print(f"Temperature in Fahrenheit to Celsius {tem}")
    case 3:
        tem=tem+273.15
        print(f"Temperature in Celsius to Kelvin {tem}")
    case 4:
        tem=tem-273.15
        print(f"Temperature in Kelvin to Celsius {tem}")