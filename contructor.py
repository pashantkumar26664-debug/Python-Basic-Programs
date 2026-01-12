

class student:
    batch= 2024                               #class attributes
    degree= "B.Sc."    
    college= "CCS UNIVERSITY"

    def __init__(self, name):
        self.name= name
        print("Students Details:")   #special method/constructor which is called automatically when object is created
    
    def getInfo(cl):                             #method creation
        print("This is college info",cl.college)

    @staticmethod
    def greet():                               #method creation
        print("Hello")


detail= student("Prashant Kumar")                           #object creation
# name= "Prashant Kumar"                         #Instance attribute 
print(detail.name,"\nBatch:", detail.batch, "\nDegree:", detail.degree, "\nCollege:", detail.college)  
