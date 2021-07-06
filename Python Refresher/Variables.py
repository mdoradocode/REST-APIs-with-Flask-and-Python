x = 12
##Creates the  value 15, THEN binds it to x, assignment happens right to left
##With Strings, you can use single or double qutation marks
name = "Wheezer"
name = 'Wheezer'

print(name * 6)
print (name + name + name)

a = 25
##25 is special, its under 255, so its created as python starts up
b = a
##b is bound to the current value of a, 25, and is not any form of a pointer like in C
a = 17

print(a)
print(b)