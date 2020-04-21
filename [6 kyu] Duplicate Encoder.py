def duplicate_encode(word):
    result = ''
    word = word.lower()
    for i in word:
        if word.count(i) > 1:
            result += ')'
        else:
            result += '('
    return result
