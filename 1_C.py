# Задача С
n = int(input())
count = 0

for i in range(n):
  x = int(input())
  count += x // 4

  if x % 4 <= 2:
    count += x % 4
  else:
    count += 2

print(count)