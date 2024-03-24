# Задача C
N = int(input())
length = [int(x) for x in input().split()]

max = length[0]
sum = 0

for i in range(N):
  if length[i] > max:
    max = length[i]
  sum += length[i]

res = max - (sum - max)

if res <= 0:
  print(sum)
else:
  print(res)