# Задача G
file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()

x = int(lines[0])
y = int(lines[1])
p = int(lines[2])

round = 1
m = 0
  
y -= x
if y > 0:
  m = p

def check(x, m):
  r = 0

  while x > 0 and m > 0:
    m -= x
    if m > 0:
      x -= m
    r += 1

  if x <= 0:
    return -1
  else:
    return r

def st1(x, y, m):
  if m > 0:
    m -= x
    if m < 0:
      if y > 0:
        y -= abs(m)
      m = 0
  return x, y, m

def test(a, b):
  while a > 0 and b > 0:
    b -= a
    if b > 0:
      a -= b
  if a <= 0:
    return False
  else:
    return True
    
if (y == x and x == p) or (y > x and x <= m):
  x = -1
elif (m > 0) and (y - x) < 0 and (m - abs(y - x)) <= 1.5 * (x - (m - abs(y - x))):
  round += check(x - (m - abs(y - x)), m - abs(y - x)) + 1
else:
  if y >= x:
    round += (y - x) // (abs(m - x)) 

    if (y - x) % (abs(m - x)) != 0:
      round += 1
      y = (x +(y - x) % (abs(m - x))) - abs(m - x)
    else:
      y = x
  else:
    if m >= x:     
      y -= x
      m -= abs(y)
      x -= m
      
      r = check(x, m)
      if r != -1:
        round += r + 1
        y = 0
        m = 0
      else:
        round = -1
        x = 0
    
  while (y > 0 or m > 0) and x > 0:
    
    round += 1
    
    if test(x - (m - abs(y - x)), m - abs(y - x)) == False:
      x, y, m = st1(x, y, m)
    else:
      check_1 = check(x - (m - abs(y - x)), m - abs(y - x))
      x1, y1, m1 = st1(x, y, m)

      if m1 > 0:
        x1 -= m1
      if y1 > 0:
        m1 += p

      m1 -= abs(y1 - x1)
      if m1 > 0:
        x1 -= m1

      y = 0
      m = 0     
      if m1 > 0 and x1 > 0:
        check_2 = check(x1, m1)
        if check_2 != -1:
          check_2 += 1
          if (check_2 < check_1):
            round += check_2
          else:
            round += check_1
        else:
          round += check_1
      else:
        round += check_1

    if m > 0:
      x -= m

    if y > 0:
      m += p

if x <= 0:
  round = -1

file1.write(str(round))

file.close
file1.close