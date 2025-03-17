class Cons:
    '''Default constructor'''
    def __init__(self):
        self.a=100
        self.b=200
        self.make = "Toyota"
    def add(self,a,b):
        print(a+b)

class Pcons:
    '''Parametriced constructor'''
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sub(self,a,b):
        print(a-b)
if __name__ == '__main__':
    cons = Cons() #default construcator
    cons.add(cons.a, cons.b) #default construcator
    pcons = Pcons(10, 20) #parametriced constructor
    pcons.sub(pcons.a, pcons.b) #parametriced constructor

