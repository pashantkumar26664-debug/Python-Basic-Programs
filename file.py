# str= "\n Reacher"
# f=open("D:\\Prashant Pc 2\\Document\\You.txt","a") #append mode
# f=open("D:\Prashant Pc 2\Document\You.txt","w") #write mode and creates file if not exists
# f.write(str)
f=open("D:\\Prashant Pc 2\\Document\\You.txt","r") #read mode
data=f.read()
print(data)
f.close()