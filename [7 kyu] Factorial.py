def factorial(n):
    result = 1
    if -1 < n < 13:
        for i in range(1, n + 1):
            result *= i
        return result
    raise ValueError
