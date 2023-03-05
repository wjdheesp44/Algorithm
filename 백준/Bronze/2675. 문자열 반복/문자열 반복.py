cnt = int(input())

for i in range(cnt):
  inputs = list(map(str, input().split()))
  num = int(inputs[0])
  
  alphabet = list(inputs[1])
  result = []

  for j in alphabet:
    for k in range(num):
      result.append(j)

  print(''.join(s for s in result))