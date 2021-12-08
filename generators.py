def simpleFunction():
    print("hello world 1")
    yield 1
    print("hello world 2")
    yield 2
    print("hello world 3")
    yield 3
    

x = simpleFunction()
print(next(x))

"""
this funtion run until the yield and stop then next() is called
go to next yield it will return yield values

"""

def simpleGenarator(limit):
    for i in range(limit):
        yield i
        

y = simpleGenarator(10)
for j in y:
    print(j)