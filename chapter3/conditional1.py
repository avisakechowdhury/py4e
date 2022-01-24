
h = float(input("Enter Hours:"))
r = float(input("Enter Rate :"))

if h > 40:
    print(40*r + (h-40)*1.5*r)
else:
    print(h*r)
