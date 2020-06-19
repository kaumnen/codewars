def series_sum(n):
    result = 0
    for i in range(1, n * 3, 3):
        result += 1 / i
    return f'{result:.2f}'
