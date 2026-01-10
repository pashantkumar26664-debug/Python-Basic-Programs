marks={"Kajal": 85, "Rahul": 92, "Priya": 78, "Amit": 90}
# print(marks["Rahul"])  # Output: 92
# print(type(marks))  # Output: <class 'dict'>
# print(len(marks))  # Output: 4
# print(marks.keys())  # Output: dict_keys(['Kajal', 'Rahul', 'Priya', 'Amit'])
# print(marks.values())  # Output: dict_values([85, 92, 78, 90])
# print(type(marks.keys()))  # Output: <class 'dict_keys'>
# print(marks.items())  # Output: dict_items([('Kajal', 85), ('Rahul', 92), ('Priya', 78), ('Amit', 90)]
# a=marks
# print(a)
# marks.update({"Kajal": 95, "Rahul": 93, "Prashant": 88})
# print(marks)  
# marks.pop("Priya")
print(marks)
print(marks.get("Amit2")) # Output: None, since "Amit2" does not exist in the dictionary
# print(marks["Amit2"]) # This will raise a KeyError because "Amit2" does not exist in the dictionary
clear_marks=marks.copy() # create a copy of the dictionary
# print(marks)
print(clear_marks)
clear_marks.clear() # clear all items from the dictionary
print(clear_marks)
