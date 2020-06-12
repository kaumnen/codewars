def to_camel_case(text):
    
    text = text.replace('-', '@')
    text = text.replace('_', '@')
    text = text.split('@')
    
    try:
        if not text[0][0].islower():
            result = text[0].title()
        else:
            result = text[0]
    except:
        result = ''
    for i in text[1:]:
        result += i.title()
        
    return result
