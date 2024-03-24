# Задача E
import sys
sys.set_int_max_str_digits(0)

n, k, d = map(int, input().split())

if d != 0:
  n *= 10
  x = 0

  flag = False

  while flag == False and x <= 9:
    if (n + x) % k == 0:
      flag = True
      n += x   
    x += 1    
  if flag == False:
    n = -1
  else:
    n *= 10 ** (d - 1)

print(n)