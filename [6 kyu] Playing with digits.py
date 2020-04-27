def dig_pow(n, p):
    str1 = str(n)
    result = 0
    
    for x in str1:
    
        result += int(x) ** p
        p += 1
        
    return result // n if result % n == 0 else -1
