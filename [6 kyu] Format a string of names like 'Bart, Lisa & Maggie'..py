def namelist(names):
    result = ''
    if len(names) == 1:
        return names[0]['name']
        
    for i in range(len(names)):
        
        result += names.pop(0)['name']
        if len(names) > 1 and names:
            result +=  ', '
        if len(names) == 1:
            result +=  ' & '
          
    return result
