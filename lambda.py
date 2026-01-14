students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# Sort the list of tuples by the second element (age)
sorted_students = sorted(students, key=lambda x: x[1])
# sorted_students is [('Tobias', 22), ('Emil', 25), ('Linus', 28)]
print(sorted_students)

