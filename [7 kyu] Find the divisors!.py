def divisors(integer):   
    result = [x for x in range(2, integer) if integer % x == 0]
    if result:
        return result
    else:
        return f'{integer} is prime'
