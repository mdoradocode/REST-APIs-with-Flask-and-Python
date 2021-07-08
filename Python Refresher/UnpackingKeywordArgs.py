def named(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named(**details)

def printNicely(**kwargs):
    named2(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

def named2(**kwargs):
    print(kwargs)

printNicely(**details)

def both(*args, **kwargs):
    print(args)
    print(kwargs)

    
both(1,3,5,name="Bob",age="25")