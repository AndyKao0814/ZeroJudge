def prime(n):
  if n == 1:
      return 0       #return 0代表回傳False return 1代表回傳True
  else:
      if n % 2 == 0 and n != 2:
        return 0
      else:
        if n % 3 == 0 and n != 3:
                return 0
        else:
          for i in range(5, int(n**0.5)+1, 6):
            if n % i == 0: #5 11 17
              return 0
            if n % (i+2) == 0: #7 13 19
              return 0            
  return 1        
while True:
  try:
    a, b = map(int, input().split())        
    if b - a > 1000:
      print(0)
      break        
    count = 0
    for i in range(a, b+1):
      count += prime(i)                
    print(count)        
  except(EOFError):
    break
