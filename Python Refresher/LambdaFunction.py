def add(x, y):
    return x + y

print(add(5,7))

## OR

addLam = lambda x,y: x+y
##meant to be short functions with maybe no name 


def double(x):
    return x * 2

sequence = [1,3,5,7,9]
doubled = [double(x) for x in sequence]
doubledWMap = map(double, sequence)
##Map applies a function onto all the elements of the list, tuple, or set. it returns a map object, so use a type definition to force them into a variable type

doubledWMapLam = list(map(lambda x: x * 2, sequence))