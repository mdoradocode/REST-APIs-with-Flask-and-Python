
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

usernameMapping = {user[1]: user for user in users}
##This gets the username for user[1] and associating that name with the whole user tuple for each user
##The user name becomes the keys and the values become all the user information
print(usernameMapping["Bob"])

usernameInput = input("What is your Username? ")
passwordInput = input("What is your Password? ")

_, username, password = usernameMapping[usernameInput]

if passwordInput == password:
    print("You are correct!")
else:
    print("Go away!")