def comp(array1, array2):
    print(array1, array2)
    
    if array2 == [] and array1 == []:
        return True
        
    if array2 == None or array1 == None:
        return False
        
    for i in array2:
    
        if i ** 0.5 in array1 or -(i ** 0.5) in array1:
        
            try:
                array1.pop(array1.index(i ** 0.5))
                array1.pop(array1.index(-(i ** 0.5)))
                
            except:
                pass
                
        else:
            return False
            
    return True
