def pig_it(text):

    return ' '.join([x[1:] + x[0]  + 'ay' if 65 <= ord(x[0]) <= 122 else x for x in text.split(' ')])
