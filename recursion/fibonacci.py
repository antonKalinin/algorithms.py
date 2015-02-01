"""
    This is a comparison of recursive and iterative methods
    of generation fibonacci numbers
"""

import cProfile


def fibonacci_recursive(n, numbers=None):
    if numbers is None:
        numbers = [0, 1]

    numbers.append(numbers[-2] + numbers[-1])

    if len(numbers) == n:
        return numbers

    return fibonacci_recursive(n, numbers)


def fibonacci_iterative(n):
    numbers = [0, 1]
    i = n - 2

    while i > 0:
        numbers.append(numbers[-2] + numbers[-1])
        i -= 1

    return numbers


if __name__ == "__main__":
    pr = cProfile.Profile()

    print('Computing 100 first fibonacci numbers.')

    print('Fibonacci recursive: ', fibonacci_recursive(100))
    cProfile.run('fibonacci_recursive(100)')

    print('Fibonacci iterative: ', fibonacci_iterative(100))

    cProfile.run('fibonacci_iterative(100)')


