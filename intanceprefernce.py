# creating a class named student
#Instance attribute , take preference over class attribute if both have same name.

class student:
    batch= 2024                               #class attributes
    degree= "B.Sc."    
    college= "CCS UNIVERSITY"

Prashant= student()                           #object creation
Prashant.college= "RMP University"                             #Instance attribute
name= "Prashant Kumar"                         #Instance attribute 
print(name,"\nBatch:", Prashant.batch, "\nDegree:", Prashant.degree, "\nCollege:", Prashant.college)  
