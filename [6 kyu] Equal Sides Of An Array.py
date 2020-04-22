def find_even_index(arr):
    counter = -1
    res = -1 #-1 is going to be returned if there aint any matches
    cases = 0
    
    for number in arr:
        counter += 1 #since .index method always returns 1st index matched, there was a problem when multiple instances of same number occured
        
        if sum(arr[:counter]) == sum(arr[counter + 1:]):
           
            cases += 1
            
            if cases > 1: #if there was more than one correct matches, return the first match
                res = arr.index(number)
                
            else: #if there were none, im returning current index as a result
                res = counter
        
    return res
