def iq_test(numbers):
    temp = []
    temp1 = []
    temp2 = numbers.split(' ')
    for i in temp2:
        if int(i) % 2 == 0:
            temp.append(i)
        else:
            temp1.append(i)
    
    if len(temp) < len(temp1):
        lower = temp
    else:
        lower = temp1
    
    return temp2.index(lower[0]) + 1
