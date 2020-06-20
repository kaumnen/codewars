def rgb(r, g, b):
    result = ''
    for i in [r,g,b]:
        try:
            if int(hex(i)[2:]) < 10:
                result += '0'
            elif len(hex(i)[2:]) == 1:
                result += '0'
        except:
            pass
        
        if i < 0:
            result += '00'
        elif i > 255:
            result += 'FF'
        else:
            result += hex(i)[2:]
        
    return result.upper()
