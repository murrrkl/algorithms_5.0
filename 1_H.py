L, x1, v1, x2, v2 = map(int, input().split())

if v1 == 0 and v2 == 0 and x1 != x2:
  print("NO")
elif x1 == x2 or (L - x1) == x2 or (L - x2) == x1:
  print("YES")
  print("0")
elif v1 == v2:
  t = -1
  t1 = (L - x1 - x2) / (v2 + v1) 
  if v1 > 0:
    t2 = (2 * L - x1 - x2) / (v2 + v1)
  else:
    t2 = (x1 + x2) / (- v1 - v2)

  if t2 > 0 and t1 > 0:
    t = min(t1, t2)
  elif t2 > 0:
    t = t2
  elif t1 > 0:
    t = t1

  if t > 0:
    print("YES")
    print(t)
  else:
    print("NO")  

elif v1 == 0:
  # Стоит правее
  if x1 > x2:
    #  Бежит по часовой стрелке
    if v2 > 0:
      t1 = (x1 - x2) / v2 # Добраться до x1
      t2 = ((L - x1) - x2) / v2 # Добиться равного расстояния слева
    else:
    #  Бежит против часовой стрелки
      t1 = ((L - x1) + x2) / abs(v2) # Добраться до x1
      t2 = (x2 - (L - x1)) / abs(v2)    
  # Стоит левее
  else:
    #  Бежит по часовой стрелке
    if v2 > 0:
      t1 = ((L - x2)  + x1) / v2 # Добраться до x1
      t2 = ((L - x1) - x2) / v2 # Добиться равного расстояния справа
    else:
    #  Бежит против часовой стрелки
      t1 = (x2 - x1) / abs(v2) # Добраться до x1
      t2 = (x2 - (L - x1)) / abs(v2)
  if t2 > 0:
    t = min(t1, t2)
  else:
    t = t1
  print("YES")
  print(t)     
elif v2 == 0:
  # Стоит правее
  if x2 > x1:
    #  Бежит по часовой стрелке
    if v1 > 0:
      t1 = (x2 - x1) / v1 # Добраться до x2
      t2 = ((L - x2) - x1) / v1 # Добиться равного расстояния слева
    else:
    #  Бежит против часовой стрелки
      t1 = ((L - x2) + x1) / abs(v1) # Добраться до x1
      t2 = (x1 - (L - x2)) / abs(v1)   
  # Стоит левее
  else:
    #  Бежит по часовой стрелке
    if v1 > 0:
      t1 = ((L - x1)  + x2) / v1 # Добраться до x1
      t2 = ((L - x2) - x1) / v1 # Добиться равного расстояния справа
    else:
    #  Бежит против часовой стрелки
      t1 = (x1 - x2) / abs(v1) # Добраться до x1
      t2 = (x1 - (L - x2)) / abs(v1)
  if t2 > 0:
    t = min(t1, t2)
  else:
    t = t1
  print("YES")
  print(t)
else:
  # Скорости разные
  # бегут в одну сторону
  if (v1 > 0 and v2 > 0) or (v1 < 0 and v2 < 0):
    if x1 < x2:
      t1 = (x1 - x2) / (abs(v2) - abs(v1)) # Попытка догнать
    else:
      t1 = (x2 - x1) / (abs(v1) - abs(v2))    

    if v1 > 0:
      t2 = ((2 * L) - x1 - x2) / (v1 + v2) # a == b при переходе на новый круг
    else:
      t2 = (x1 + x2) / (- v1 - v2)
    t3 = (L - x1 - x2) / (v1 + v2) # a == b при равных интервалах на первом круге      
  else:
    #  Бегут в разные стороны
    t1 = -1
    t2 = -1
    t3 = -1
    
    if v1 == abs(v2) or v2 == abs(v1):
      if (x1 < x2 and v1 > 0) or (x2 < x1 and v2 > 0):
        t1 = abs(x1 - x2) / (abs(v1) * 2)
      if (v2 > 0):
        t2 = (L - x2 + x1) / (2 * abs(v1))
        t3 = (x2 - x1 - L) / (-2 * abs(v1))
      else:
        t2 = (L - x1 + x2) / (2 * abs(v1))
        t3 = (x1 - x2 - L) / (-2 * abs(v1))
    else:    
      t1 = (L - x2 - x1) / (v1 + v2) # a == b на первом круге
  
      # Второй бежит по часовой
      if v2 > 0:
        t2 = (x1 - x2 + L) / (v2 - v1) # после смены круга
        t3 =  (x2 - x1) / (v1 - v2) #  Попытка встречи
      else:
        t2 = (x2 - x1 + L) / (v1 - v2) # после смены круга
        t3 =  (x1 - x2) / (v2 - v1) #  Попытка встречи

  t = -1

  if t1 < 0:
    t = t2
  elif t2 < 0:
    t = t1
  elif t1 > 0 and t2 > 0:
    t = min(t1, t2)

  if t < 0 and t3 > 0:
    t = t3
  elif t > 0 and t3 > 0:
    t = min(t, t3)

  if t > 0:
    print("YES")
    print(t)
  else:
    print("NO")