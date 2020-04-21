def find_outlier(integers):
    even = 0 
    odd = 0
    for i in integers: #checking if array is mostly even or odd
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if even > odd: #checking what type of array i have, and therefor returning appropriate integer
        for i in integers:
            if not i % 2 == 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i
