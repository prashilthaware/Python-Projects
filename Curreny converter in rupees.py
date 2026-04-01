print("Curreny converter in rupees")
rupees=float(input("Enter amount in rupees:"))
print("1.USD")
print("2.EURO")
print("3.GBP")
print("4.JPY")
opt=float(input("Enter option:"))

match opt:
    case 1:
        usd=0.012*rupees
        print(f"currency in USD: {usd}")
    case 2:
        euro=0.010*rupees
        print(f"currency in EURO: {euro}")
    case 3:
        gbp=0.0088*rupees
        print(f"currency in GBP: {gbp}")
    case 4:
        jpy=1.71*rupees
        print(f"currency in JPY: {jpy}")