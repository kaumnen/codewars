def sort_array(source_array):
    temp = []
    temp1 = 0
    for i in range(len(source_array)):
        try:
            if not source_array[i] % 2 == 0:
                temp.append(source_array[i])
                source_array[i] = 'a'
        except IndexError:
            pass
    temp = sorted(temp)
    for j in range(len(source_array)):
        try:
            if source_array[j].isalpha():
                source_array[j] = temp[temp1]
                temp1 += 1
        except AttributeError:
            pass
    return source_array
