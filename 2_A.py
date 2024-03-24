# Задача A
K = int(input())

x1, y1 = map(int, input().split())
x2, y2 = x1, y1

for i in range(K-1):
  x, y = map(int, input().split())

  if x < x1:
    x1 = x
  if y < y1:
    y1 = y
  if x > x2:
    x2 = x
  if y > y2:
    y2 = y

print(x1, y1, x2, y2)