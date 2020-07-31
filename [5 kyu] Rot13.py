def rot13(message):
    result = ''
    for i in message:
        if i.isalpha():
            if ord(i.lower()) + 13 > 122:
                result += chr(ord(i) - 13);
            else:
                result += chr(ord(i) + 13);
        else:
            result += i;
    return result
