a="abcdefghijklmnopqrstuvwxyz"
b=a[1:20] #slicing
c=a[::2] #step slicing
print(c)
print(b)
print(len(a)) #length of string
print(a.capitalize()) #first letter capital
print(a.lower()) #all letters small
print(a.endswith("xyz")) #check string ends with given value
print(a.upper()) #all letters capital
print(a.find("mno")) #index of given value
print(a.isalpha()) #check all letters are alphabetic
print(a.islower()) #check all letters are small
print(a.isupper()) #check all letters are capital
print(a.replace("abc","123")) #replace given value with new value
print(a.strip()) #remove extra spaces
print(a.split("def")) #split string at given value
print(a.swapcase()) #swap lower case to upper case and vice versa
print(a.upper()) #convert to upper case
print(a.title()) #first letter of each word capital
print(a.index("pqr")) #index of given value
print(a.count("a")) #count occurrences of given value
print(a.center(30,"*")) #print string at center with given fill character
print(a.startswith("abc")) #check string starts with given value
print(a.rfind("uvw"))  #index of last occurrence of given value
print(a.partition("mno")) #print tuple of 3 parts
print(a.replace("xyz","789")) #replace given value with new value