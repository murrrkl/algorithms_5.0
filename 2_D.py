# Задача D
file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()

N = int(lines[0])
current = [0] * 8
prev = [0] * 8

r, c  = map(int, lines[1].split())
current[c-1] = 1

P = 4

for i in range(2, N + 1):
  x, y = map(int, lines[i].split())
  if x == r: # По одной строке
    if current[y-2] != 1: # Слева нет соседа
      P += 2
    if prev[y-1] != 1: # Снизу никого
      P += 2
    current[y-1] = 1
  else:
    # Новая строка
    r = x
    P += 2
    prev = current.copy()
    current = [0] * 8
    current[y-1] = 1
    if prev[y-1] != 1: # Снизу никого
      P += 2
  
file1.write(str(P))
file1.close
file.close