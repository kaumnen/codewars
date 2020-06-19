def valid_parentheses(string):
    temp = [1]
  
    for i in string:
        if i == ')':
            if temp[-1] == '(':
                temp.pop(-1)
            else:
                return False
        elif i == '(':
            temp.append(i)
            
    if temp == [1]:
        return True
    return False
