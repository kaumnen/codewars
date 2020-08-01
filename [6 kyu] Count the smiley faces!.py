def count_smileys(arr):
    eyes = [":", ";"];
    nose = ['-', '~']
    mouth = [')', 'D']
    result = 0
    
    for i in arr:
        if len(i) == 2:
            if i[0] in eyes and i[1] in mouth:
                result += 1
        elif len(i) == 3:
            if i[0] in eyes and i[1] in nose and i[2] in mouth:
                result += 1
    return result
