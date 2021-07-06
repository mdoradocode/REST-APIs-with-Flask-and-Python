number = 7
user_input = input("Enter y if you would like to play (Y/n): ")
while user_input != "n":
    userNumber = int(input("Guess the number"))
    if userNumber == number:
        print("You guessed correct")
        break
    elif abs(number - userNumber) == 1:
        print("You were off by one")
    else:
        print("You guessed wrong")
    user_input = input("Enter y if you would like to play (Y/n): ")

friends = ["Rolf", "Jen", "Bob"]

for friend in friends:
    print(f"{friend} is my friend")
for friend in range(4):
    print(f"{friend} is my friend")
##Friend is a created variable that allows you to apply to the diffent places in the for loop to the vaiable