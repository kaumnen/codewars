def printer_error(s):
    result = 0
    for i in s:
        if not 97 <= ord(i) <= 109:
            result += 1
    return f'{result}/{len(s)}'
