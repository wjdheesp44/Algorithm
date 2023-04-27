n, k = map(int, input().split())
coin_types = []
cnt = 0

for i in range(n):
  coin_types.append(int(input()))
coin_types = sorted(coin_types, reverse=True)

for coin in coin_types:
  cnt += k // coin
  k %= coin
  
print(cnt)