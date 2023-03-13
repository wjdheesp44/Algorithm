num = int(input())
words = []

for i in range(num):
  word = str(input())
  words.append(word)

words = sorted(list(set(words)))
words.sort(key=len)
for i in words:
  print(i)  