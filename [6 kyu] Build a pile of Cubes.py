def find_nb(m):
    result = 0
    i = 1
    while result <= m:
        result += i ** 3
        i += 1
        if result == m:
            return i - 1
    return -1
