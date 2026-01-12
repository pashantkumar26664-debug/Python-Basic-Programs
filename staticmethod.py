#static method example
#not taking class $ object attributes

class student:
    batch= 2024                               #class attributes
    degree= "B.Sc."    
    college= "CCS UNIVERSITY"
    
    def getInfo(cl):                             #method creation
        print("This is college info",cl.college)

    @staticmethod
    def greet():                               #method creation
        print("Hello")

Prashant= student()                           #object creation
Prashant.college= "RMP University"                                    #Instance attribute 

Prashant.greet()      #calling method using object
Prashant.getInfo()   