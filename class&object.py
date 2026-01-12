# creating a class named student

class student:
    batch= 2024                               #class attributes
    degree= "B.Sc."    
    college= "CCS UNIVERSITY"

Prashant= student()                           #object creation
name= "Prashant Kumar"                         #Instance attribute 
print(name,"\nBatch:", Prashant.batch, "\nDegree:", Prashant.degree, "\nCollege:", Prashant.college)  

Lucky= student()
name= "Lucky Patel"
print(name,"\nBatch:", Lucky.batch, "\nDegree:", Lucky.degree, "\nCollege:", Lucky.college)


#Instance attributes are specific to each object whereas class attributes are shared among all objects of the class.
#Instance attribute , take preference over class attribute if both have same name.