num = int(input())

def fibonacci(num):
  a = 0
  b = 1
  c = 0
  if num == 0:
    return a
  
  for i in range(num):
    a = b
    b = c
    c = a + b
    
  return c

print(fibonacci(num))