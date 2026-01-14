numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers is [2, 4, 6]   used for filter(): Used to filter elements from an iterable based on a condition
print(even_numbers)

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  #used for map(): Used to apply a transformation to every item in an iterable
# squared_numbers is [1, 4, 9, 16, 25]
print(squared_numbers)