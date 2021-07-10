#A first class function just means that functions can be passed as arguments to functions.
def calculate(*values, operator):
    return operator(*values)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"
##Passing the divide as the value of the function (its name and space in memory) divide is first class function
result = calculate(20, 4, operator=divide)
print(result)


##Get_friend_name is the finder, which will run on each element of the sequence (friends) and try to find the expected value (Bob Smith)
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Bob Smith", get_friend_name))
##Could be done this way with a lambda function
##print(search(friends, "Bob Smith", lambda friend: friend["name"]))
##Or
##print(search(friends, "Rolf Smith", itemgetter("name")))