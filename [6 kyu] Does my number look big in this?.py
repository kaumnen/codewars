def narcissistic( value ):
    for i in range(10):
        res = sum([int(x) ** i for x in str(value)])
        if res == value:
            return True
    return False
