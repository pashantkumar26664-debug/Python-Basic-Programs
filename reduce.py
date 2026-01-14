from functools import reduce
numbers = [3, 2, 5, 4, 1]
max_element = reduce(lambda x, y: x if x > y else y, numbers)
print(max_element)
# Output: 5

from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)
# Output: 15

