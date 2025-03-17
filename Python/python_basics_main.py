### Topics to learn in python
import create_class
class python():
    def python_class(self, level_1=0, level_2=0, level_3=0):

        '''
        1. Class level
            1. How to create a class *
            2. How to create a constructor *
            3. Why do we create if __name__==__main__:? *
            4. How to create a function *
            5. Why do we use self?
            6. How to create and call modules
            7. Why do we create __init__.py in folder?
        '''
        print("inside")

        if level_1 == 1:
            if level_2 == 1:
                if level_3 == 1:
                    cc = create_class.basic_example()
                    print(cc.example1(10, 20))

if __name__=='__main__':
    level_0 = int(input("1. Class 2. Utility Functions:"))
    level_1 = int(input("input Level 1(Basic):"))
    level_2 = int(input("Input level 2(Modorate):"))
    level_3 = int(input("Input level 3(Complex):"))
    if level_0 == 1:
        p = python()
        p.python_class(level_1, level_2, level_3)









'''
2. Utility functions
    1. Zip
    2. Lambda
    3. decorator
    4. Range
    5. Enumerate
    6. Map
    7. Comprehension
3. File Handling Functions
    1. Open
    2. Read
    3. Write
    4. Close
4. Dictionary Functions
    1. Keys
    2. values
    3. items
    4. get
5. List Functions
    1. Append
    2. Extend
    3. Pop
    4. Sort
6. String Functions
    1. Str
    2. Upper
    3. Lower
    4. Split
7. Mathematical Functions
    1. Abs
    2. Round
    3. Max
    4. Min
8. Basic Funcitons
    1. Print
    2. Len
    3. Type
    4. Input 
'''