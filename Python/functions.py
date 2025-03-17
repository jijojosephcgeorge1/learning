from functools import reduce
def add(a, b):
    print(a+b)

add(10,50)
def args(*args):
    return reduce((lambda x, y: x + y), args)

print(args(1,2,3,5))


def kwargs(**kwargs):
    a=0
    for key, value in kwargs.items():
        a+=value
    print(a)
kwargs(a=1,b=2,c=3)