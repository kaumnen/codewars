def tribonacci(signature, n):
    if n == 0 : return []
    
    elif n < 4:
        return [signature[n] for n in range(n)]
        
    else:
        result = signature
        
        for i in range(n - 3):
            result.append(sum(result[-3:]))
            
        return result
