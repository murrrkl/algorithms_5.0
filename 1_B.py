# Задача B
g1, g2 = map(int, input().split(":"))
g3, g4 = map(int, input().split(":"))
t = int(input())

result = 0
G1 = g1 + g3 # Общий счёт нашего игрока
G2 = g2 + g4 # Общий счёт противника

if G1 <= G2:
  result = G2 - G1 # Для уравнивания счёта

  if t == 2:
    if g4 >= g1:
      result += 1
  else:
    g3 += result

    if g2 >= g3:
        result += 1

print(result)