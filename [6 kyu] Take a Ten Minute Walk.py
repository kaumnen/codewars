def is_valid_walk(walk):
    
    if len(walk) == 10:
        temp = list(set(walk))
        
        if walk.count(temp[0]) == walk.count(temp[1]):
            if len(temp) == 4:
                if walk.count(temp[2]) == walk.count(temp[3]):
                    return True
                else: return False
            else: return True
        else:
            return False
    else:
        return False
