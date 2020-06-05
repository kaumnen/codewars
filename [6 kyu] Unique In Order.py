def unique_in_order(iterable):
    result = []
    prev = None
    
    for i in range(len(iterable)):   
    
        if not prev == iterable[i]:
            result.append(iterable[i])
            prev = iterable[i]
            
        else:
            pass
            
    return result
