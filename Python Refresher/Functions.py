def hello():
    print("Hello you filthy animal!")

hello()

def userAgeInSeconds():
    userAge = int(input("What is your age? "))
    ageInSeconds = userAge * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {ageInSeconds}.")

userAgeInSeconds()

print("Goobye!")

# -- Don't reuse names, it's generally confusing! --
friends = ["Rolf", "Bob"]

##Python has a pass by object reference, in which function calls have different memory areas but modify the same data, think of the box example. When a function uses a variable, its given its own box, seperate from the box of the original variable, but both the boxes have the SAME data in the, modify one, modify the other
##def add_friend():
    ##friend_name = input("Enter your friend name: ")
    ##friends = friends + [friend_name]  # Another way of adding to a list!
