def move_zeros(array):
    i = 0
    cnt = array.count(0)
    if cnt > 10:
        cnt -= 1
    while i < len(array) - cnt:
        
        if array[i] is not False and array[i] == 0:
            array.append(array.pop(i))
            i -= 1
    
        i += 1
    
    return array
