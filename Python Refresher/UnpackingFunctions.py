##This function has a tuple of arguements that need to be collected
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total
print(multiply(1, 3, 5))

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(*args)
    else:
        return "No valid operator provided to apply()."

print(apply(1,3,5,7, operator="*"))

##Pass one parameter at a time
def add(x, y):
    return x + y

nums = [3,5]
print(add(*nums))

##With a dictionary pass in each arguement with each key of the dictionary::Keyword args need the double stars
nums = {"x": 6, "y": 4}
print(add(**nums))


