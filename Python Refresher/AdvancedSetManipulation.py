friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
##If building a one element set, put a comma after to show that it is not doing any math 


localFriends = friends.difference(abroad)
##This takes the elements of abroad and subtracts them from the friends elements
localFriendsEXAMPLE = abroad.difference(friends)
##This takes the elements of friends out of the abroad elements and give the results, an empty list
print(localFriends)
print(localFriendsEXAMPLE)

friends = localFriends.union(abroad)
print(friends)

both = friends.intersection(abroad)
print(both)

