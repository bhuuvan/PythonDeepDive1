# *args
a,b, *c = 10, 20, 'a','b'
print(a)
print(b)
print(c)


def func1(a,b,*c):
    print(a)
    print(b)
    print(c)


func1(10,20)

func1(10,20,1,2,3)

def func2(a,b,*args):
    print(a)
    print(b)
    print(args)

def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count

print(avg(10,20))
print(avg())


def avg1(*args):
    count = len(args)
    total = sum(args)
    #Short circuitng using Boolean AND
    return count and total/count


print(avg1(10,20,30))
print(avg1())


def avg2(a,*args):
    count = len(args) +1
    total = sum(args)
    #Short circuitng using Boolean AND
    return total/count


print(avg2(10,20,30))


def func3(a,b,c):
    print(a)
    print(b)
    print(c)
l = [10,20,30]


# unpacking the list using *l
func3(*l)


def func4(a,b,c,*args):
    print(a)
    print(b)
    print(c)
    print(args)
l = [10,20,30,40,50]


# unpacking the list using *l
func4(*l)