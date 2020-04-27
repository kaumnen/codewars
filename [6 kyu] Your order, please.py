def order(sentence):
  
  dict = {}
  arr = sentence.split(' ')
  
  for i in arr:
      
      for p in range(len(i)):
          
          if i[p].isdigit():
              dict[int(i[p])] = i          
  
  return ' '.join(dict[x] for x in sorted(dict))
