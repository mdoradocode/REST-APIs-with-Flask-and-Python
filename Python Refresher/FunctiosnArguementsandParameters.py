def add(x, y):
    result = x + y
    print(result)
add(5,3)

def sayHello(name, surname):
    print(f"Hello, {name} {surname}")

sayHello(surname="Bob", name="Smith")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("You Fool!")

divide(dividend=15,divisor=0)
##when you specify what value will be attached to what variable, its called a keyword argumen

## --Default Parameters--
def add(x, y=8):
    print(x +y)

add(5)
add(x=5)
add(y=5)
##Last one will fail because x needs a variable and has no default parameter, default parameters must be followed by other default parameters, you couldnt do add(x=5, y)


# -- Usually don't use variables as default value --

default_y = 3


def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)  # 5

default_y = 4
print(default_y)  # 4

add(2)  # 5, even though we re-defined default_y