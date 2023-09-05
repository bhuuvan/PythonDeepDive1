#Positonal and Keyword Arguments
def my_func(a,b,c):
    print("a={0}, b={1}, c= {2}".format(a,b,c))

my_func(9,26,7)


#by passing a default paramter
def my_func2(a,b,c=20):
    print("a={0}, b={1}, c= {2}".format(a, b, c))

my_func2(10,2)

#by passing all parameters as default
def my_func3(a=23,b=2323,c=2322):
    print("a={0}, b={1}, c= {2}".format(a, b, c))

my_func3()


#over-writing the default parameter
my_func3(a=111,b=2222,c=22222)
