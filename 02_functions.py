# functions
# def hello_func():
#     print("Hello world!")
#     name = input("What is your name? ")
#     print(f"Nice to meet you, {name}.")
# hello_func()

# functions that take parameters
# def hello_func(greeting):
#     print("Hello world!")
#     name = input("What is your name? ")
#     print(f"{greeting}, {name}.")
# hello_func("Hey whats up")

# functions that returns a value
def cube(x):
    return x*x*x
print(cube(3))

# function with a default value for a parameter
def hello_func(greeting, name=None):
    print("Hello world!")
    if name == None:
        name = input("What is your name? ")
    print(f"{greeting}, {name}.")

hello_func("Nice to meet you", "Joe")

# function with variable number of parameters
def multi_add(start, *args):
    result = start
    for x in args:
        result+=x
    return result
print(multi_add(10,4,3,2,1,4,5))


