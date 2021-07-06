name = 'Bob'
greeting = f'Hello, {name}'
##That f is an f string which allows for variables to be embbeded inside of strings in python
print(greeting)

name = 'Frank'

print(greeting)

print(f'Hello, {name}')

greeting = "Hello, {}"
with_name = greeting.format(name)
##Calls the format function (which is a constructor I think, or at least something along that line) on greeting. When with_name is called, it will have the most recent version of 'name' replacing the curly braces
print(with_name)

with_name = greeting.format('Rolf')
print(with_name)

long_phrase = 'Hello, {}. Today is {}'
formatted = long_phrase.format('Rolf','Monday')
print(formatted)