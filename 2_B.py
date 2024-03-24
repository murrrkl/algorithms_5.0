# Задач B
N, K = map(int, input().split())
price = [int(x) for x in input().split()]

coins = 0
d1 = 0

if K >= N:
  d2 = N - 1
else:
  d2 = K

while d2 < N and d1 < N - 1:
  days = price[d1+1:d2+1]
  p = max(days)-price[d1]
  if p > 0 and p > coins:
    coins = p
  d1 += 1
  if d2 < N-1:
    d2 += 1

print(coins)