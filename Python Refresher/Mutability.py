a = []
b = a
##a and b are names, with the same list object
print(id(a))
print(id(b))
a.append(35)
print(a)
print(b)

# We mutated (changed) the value, its names still point to the _same thing_, so it doesn't matter which name you use.
a = []
b = []
a.append(35)
print(a)
print(b)
# Here they are different lists, because [] creates a new list every time. You can check whether two things are the _same_ one by usingt the `id()` function:
print(id(a))
print(id(b))  # Different from id(a)


# -- immutable --
# Some values can't be changed because they don't have methods that modify the value itself.
# In case of the list, `.append()` mutates the list.
# For example integers don't have any such methods, so they are called _immutable_.

a = 8597
b = 8597

print(id(a))
print(id(b))  # Same one

a = 8598

print(id(a))
print(id(b))
##The memory location changes when variabels created near each other with the same value are changed
##Strings are immutable