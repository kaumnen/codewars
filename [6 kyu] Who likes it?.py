def likes(names):
    result = ''
    length = len(names)
    if len(names) == 0:
        return 'no one likes this'
    elif length > 3:
        return '{}, {} and {} others like this'.format(names[0], names[1], length - 2)
    
    else:
        for name in names:
            if length > 2:
                result += name + ', '
                length -= 1
            elif length == 2:
                result += name + ' and '
                length -= 1
            else:
                result += name + ' like this'
                
    if len(names) == 1:
        return result.replace('like', 'likes') 
    else: return result
