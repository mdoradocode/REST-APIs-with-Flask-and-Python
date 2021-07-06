print(5 == 5)
##A boolean comparison bascially the same as C
print(5 > 5)

print(10 != 10)
##Can use this approach on other data types but they may have weird interaction

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)
##Checks to see if the same value is held by the two list
print(friends is abroad)
##Checks to see if friends is an alias for abroad, checks to see if they have the same area in memory
print(friends is friends)
abroad = friends
print(friends is abroad)




