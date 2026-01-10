# recursion is used when a function calls itself to solve smaller instances of the same problem.

def factorial(n):
    """Calculate factorial of n using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_list(lst):
    """Calculate sum of list elements using recursion."""
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])


# Test the functions
if __name__ == "__main__":
    print(factorial(5))
    print(fibonacci(25))
    print(sum_list([1, 4, 10, 4, 5]))