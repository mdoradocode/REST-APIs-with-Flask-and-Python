name = input("What is your name? ")
print(name)
size_input = input("How big is your house is sqaure feet? ")
squareFeet = int(size_input)
squareMeters = squareFeet /10.8
print(f"The size of your house is {squareMeters:.2f} sq meters")
##The point .2f will format the syntax to two decimal places