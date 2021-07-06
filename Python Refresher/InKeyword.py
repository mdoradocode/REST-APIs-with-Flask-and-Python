friends = ["Rolf", "Bob", "Jen"]
userFriend = input("Enter the name of your friend")
print("Jen" in friends)
##Can check to see if strings are in other strings and a bunch other stuff

number = 7
user_input = input("Enter y if you would like to play: ").lower()
if user_input in ("y", "Y"):
    userNumber = input("Guess the number")
    if userNumber == number:
        print("You guessed correct")
    elif abs(number - userNumber) == 1:
        print("You were off by one")
    else:
        print("You guessed wrong")