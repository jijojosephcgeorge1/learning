def add_sub(func):
    def wrapper(a,b):
        print(a+b)
        func(a,b)
        print(a-b)
    return wrapper

@add_sub
def fun1(a,b):
    print(a/b)
fun1(10,20)

