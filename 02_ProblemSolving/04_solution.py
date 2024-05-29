# fruit = "Banana"
# color = "Yellow"

fruit = input("Enter Fruit : ")
color = input("Enter Color : ")

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")

else:
    print("No information about the fruits")