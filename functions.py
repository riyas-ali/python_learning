# function
def greet():
    print("Hi")
    name = input("What is your name?\n:")
    print(f"Good morning {name}")


greet()


# function with parameters
def add(x, y):
    total = x + y
    print(f"Total is {total}")


add(5, 4)


# function return something.
def get_value(x, y):
    return x + y


result = get_value(1, 2)
print(f"Result is {result}")
