def tickets(people):
    print(people)
    currentCash = []
    
    for i in people:
        temp = i
        
        if i == 25:
            currentCash.append(i)
            
        else:
            if not currentCash:
                return 'NO'
                
            else:
                while currentCash:
                    temp -= currentCash.pop(-1)
                    
                    if temp == 25:
                        currentCash.append(i)
                        break
                        
                if temp != 25:
                    return 'NO'
                    
        if currentCash[-1] == 100:
            currentCash.pop(-1)
            
    return 'YES'
