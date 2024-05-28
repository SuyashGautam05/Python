age =  22
day = "Wednesday"

# age = int(input("Enter your age : "))
# day = input("Enter day : ")

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2

print("Ticket price for you is $",price)