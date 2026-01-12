class student:
    batch= 2024                               #class attributes
    degree= "B.Sc."    
    college= "CCS UNIVERSITY"
 
    def getInfo(self):                             #method creation
        print("This is college info",self.college)

    def greet(self):                               #method creation
        print("Hello")

Prashant= student()                           #object creation
Prashant.college= "RMP University"                             #Instance attribute
name= "Prashant Kumar"                         #Instance attribute 
# print(name,"\nBatch:", Prashant.batch, "\nDegree:", Prashant.degree, "\nCollege:", Prashant.college)
Prashant.greet()      #calling method using object
Prashant.getInfo()   