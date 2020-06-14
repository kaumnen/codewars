import math
def is_prime(num):
  
  if num <= 0 or num == 1:
      return False
      
  else:
      temp = math.floor(num ** 0.5)

      for i in range(2, temp + 1):
      
          if num % i == 0:
              return False
              
      return True
