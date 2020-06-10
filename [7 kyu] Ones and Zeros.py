def binary_array_to_number(arr):
  result = 0
  arr = arr[::-1]
  
  while 1 in arr:
      result += 2 ** (arr.index(1))
      arr[arr.index(1)] = 0
      
  return result
