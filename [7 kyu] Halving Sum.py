def halving_sum(n): 
    result = 0
    i = 1
    while n > 0:
        result += n 
        n = n // 2
        i *= 2
    
    return result
