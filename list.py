a=["apple", "banana", "cherry",50,100,150,True,65.25,None]
print(a)
print(type(a))
print(len(a))
print(a[0])
print(a[3])
print(a[-1])
a[4]=75 #in list we can change the value of item
print(a)
print(a[1:5])
a.append("orange") #to add item at the end of list
print(a)
a.reverse() #to reverse the list
print(a)
a.remove(150) #to remove item from list
print(a)
a.pop(3)  #to remove index item from list
print(a)
a.pop()  #to remove last item from list
print(a)
a.insert(2,"kiwi") #to insert item at specific index
print(a)