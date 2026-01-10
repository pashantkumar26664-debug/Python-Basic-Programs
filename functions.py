# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# avg=(a+b+c)/3
# print(avg)

# Function to calculate average of three numbers 
# def avg(): 
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     c=int(input("Enter third number: "))
#     average=(a+b+c)/3
#     print(average)

# avg() # Call the function to execute once   

# for i in range(3): # Call the function three times or in a loop
#     avg()

def name(a):  #function with parameter argument
    print("Hello, " + a)
    return "Bye" #function with return value and it will return this value when called by another variable

b=name("Prashant") # calling function and storing return value in variable
name("Prashant")
print(b)