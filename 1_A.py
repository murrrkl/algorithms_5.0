# Задача A
q, m = map(int, input().split())

p2 = p + v
p1 = p - v

q2 = q + m
q1 = q - m

result = (v + m) * 2 + 2

if q1 >= p1 and p2 >= q2:
  result -= m * 2 + 1
elif p1 >= q1 and q2 >= p2:
  result -= v * 2 + 1  
elif p1 < q1 and q1 < p2:
  if (q1 >= 0 and p2 >= 0) or (q1 < 0 and p2 < 0):
    result -= abs(abs(p2) - abs(q1)) + 1
  else:
    result -= abs(p2) + abs(q1) + 1
elif q1 < p1 and p1 < q2:
  if (q2 >= 0 and p1 >= 0) or (q2 < 0 and p1 < 0):
    result -= abs(abs(q2) - abs(p1)) + 1
  else:
    result -= abs(p1) + abs(q2) + 1
elif p1 == q2 or p2 == q1:
  result -= 1

print(result)