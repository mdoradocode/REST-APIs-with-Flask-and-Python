l = ["Bob", "Rolf", "Anne"]
##List: can add and remove elements, keeps item in order
t= ("Bob", "Rolf", "Anne")
##Tuple: Similar to a list, difference with, cant add or remove elements from a tuple, keeps items in order
s = {"Bob", "Rolf", "Anne"}
##Set: can add and remove elements, but can't have repeat elements, order is not preserved. Cannot use subscript notation

print(l[2])

l[0] = 'smith'
l.append("Smith")
##Add to the end
print(l)

l.remove("smith")
print(l)

s.add("Smith")
s.add("Smith")
print(s)