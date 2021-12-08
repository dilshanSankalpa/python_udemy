def sampleFunction(*args, **kwargs):
    print(type(args),args)
    print(type(kwargs),kwargs)
    print(kwargs['name'])
    
sampleFunction(1,2,3,4,5,name="hello",age=18)
    
    
# can use args to enter a tuple to a function
#can use kwargs to enter a named argument to a function
#args kwargs are just naming conventions can change them
#args , kwargs should be at the end of the parameter list
#keword parameter fun(name="hello") should be after the positonal parameters