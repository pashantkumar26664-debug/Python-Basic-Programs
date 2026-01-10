x=() #empty tuple
y=(1,2,3) #tuple with integers
z=("apple","banana","cherry") #tuple with strings  
print(x)
print(y)
print(z)
print(type(y))
print(len(z))
a=(1,2,'book',3.5,True,None) #tuple with mixed data types
print(a)
print(type(a))
print(a.count(2)) #to count occurrences of an item in tuple
print(a.index('book')) #to find the index of an item in tuple
print(a[2]) #accessing item by index
b=y+z+a #concatenation of tuples
print(b)