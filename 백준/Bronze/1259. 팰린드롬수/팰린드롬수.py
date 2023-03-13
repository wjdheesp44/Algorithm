while(True):
  num = input()
  if num == '0':
    break

  result = 'no'

  if num == num[::-1]:
    result = 'yes'

  print(result)