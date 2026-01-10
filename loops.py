# for i in range(1,11):
#     i=i*2 #to print table of 2
#     print(i)

# use if else inside for loop
# for j in range(1,21): 
#     if j%2==0:
#         print(j,"is even")
#     else:
#         print(j,"is odd")    

# i=1
# while i<=10: #it is only executed when condition is true
#     print(i*3) #to print table of 3
#     i=i+1

a=(1,2,3,4,5)
a_len=len(a)
i=8 #initializing i with value greater than length of tuple to show that while loop will not execute
while i<a_len:
    print(a[i]) #to print all items of tuple using while loop
    i=i+1    

# for k in a:
#     print(k) #to print all items of tuple using for loop    

# if we want execute loop atleast once then we use do for loop with else
for i in range(0):
    print(i)
else:
    print("i is not in range anymore")