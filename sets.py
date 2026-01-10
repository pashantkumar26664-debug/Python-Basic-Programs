s={} #empty dictionary
s1=set() #empty set
s2={1,2,3,4,5,1,2,3} #set with integers
s3={"apple","banana","cherry",1,4} #set with mixed data types
# print(s)    
# print(type(s))
# print(s1)  
# print(type(s1))
print(s2) #set removes duplicate values
# s2.add(6) #to add item in set
# print(s2)
s2.remove(3) #to remove item from set
print(s2)
# s2.discard(10) #to remove item from set, no error if item not found
# print(s2)
s2.pop() #to remove a random item from set
print(s2)
# s2.clear() #to clear all items from set
print(len(s2)) #to find length of set
intersection_set=s2.intersection(s3) #to find intersection of two sets
print(intersection_set)
union_set=s2.union(s3) #to find union of two sets
print(union_set)
