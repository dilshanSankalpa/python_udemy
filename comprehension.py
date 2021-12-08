a = [1,2,3,4,5,6,7,8,9,10]
b = a
b.append(11)
#append to the both lists
print("map to the name list")
print(a,b,"\n")

c = list(a)
c.append(11)
#now only append to the c
print("using separate list")
print(a,c,"\n")

#we can map list to a set 
d = set(a)
print("using set to a map a list")
print(a,d,"\n")

#sets doesnt contain repeated values

#comprehension
e = [i for i in a]
#does the same thing as list(a) can use for lists,dictionaries,sets
print("comprehension insert")
print(a,e,"\n")

#can use a function even to change values
def multiplyByTwo(a):
    return a*2

f = [multiplyByTwo(i) for i in a]
print("comprehension with a function")
print(a,f,"\n")

#should not use with a complex function since it gets high time complexity

#can filter items with
g = [i for i in a if i%2==0]
print("using filters with comprehension")
print(a,g,"\n")

#can not be used with tuples