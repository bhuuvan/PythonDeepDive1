# Function with positional arguments
def my_func(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))

# Calling the function with positional arguments: a=9, b=26, c=7
my_func(9, 26, 7)

# Function with default parameter
def my_func2(a, b, c=20):
    print("a={0}, b={1}, c={2}".format(a, b, c))

# Calling the function with default value for 'c': a=10, b=2, c=20
my_func2(10, 2)

# Function with all default parameters
def my_func3(a=23, b=2323, c=2322):
    print("a={0}, b={1}, c={2}".format(a, b, c))

# Calling the function with all default values: a=23, b=2323, c=2322
my_func3()

# Overwriting default values using keyword arguments: a=111, b=2222, c=22222
my_func3(a=111, b=2222, c=22222)
