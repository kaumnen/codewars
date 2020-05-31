def alphabet_position(text):
    result = ''
    
    for letter in text.lower():
    
        if letter.isalpha():
            result += ' {}'.format(ord(letter)-96)
            
    return result[1:]
