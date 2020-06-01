def create_phone_number(n):
    temp = ''
    for i in n:
        temp += str(i)
    return '({}) {}-{}'.format(temp[:3], temp[3:6], temp[6:])
