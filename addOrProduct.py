def sumOrProduct(n, q):
  
  answer = 0
  mod = int(1e9) + 7
  
  if q == 1:
    answer = (n * (n + 1)) // 2
    
    
  else:
    answer = 1
    for i in range(1, n + 1):
      i %= mod
      answer %= mod
      answer = (((answer * i) % mod) + mod) % mod
      
      
  return answer
