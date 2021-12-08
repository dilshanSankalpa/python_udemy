#this is an single line comment and

"""

this
is
a
multiline comment
as well as a multiline
string

we can use multiline comments to create document comment
"""

#ex of a document comments

""" Adding two numbers
:param x -> any : first number
:param y -> any : second number
:return x+y 
:rtype: any

"""

def addTwoNumbers(x, y):
    return x + y

addTwoNumbers(2,3)

""""
can add extention to use read document comments
"""

def addNum(x:int, y:int)-> any : #this notation only for documentation and to hint not compiled and check the type
    return x + y