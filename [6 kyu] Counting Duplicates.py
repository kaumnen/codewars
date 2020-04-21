def duplicate_count(text):

    temp = []
    text = text.lower() #its case sensitive, so making sure everything is counted
    
    for i in text:
        if text.count(i) > 1 and not type(i) == int: #if there is more than one case of single LETTER:
            if not i in temp: #making sure function doesnt add same results more than once
                temp.append(i)
        
    return len(temp)
     
