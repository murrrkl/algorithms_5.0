res  = []
file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

def ParseImg(s):
  width = ""
  height = ""
  dx = ""
  dy = ""
  
  type = "e" if ("embedded" in s) else "s" if "surrounded" in s else "f" if "floating" in s else ""

  w_i = s.index("width=") + 6
  
  while s[w_i] != " " and s[w_i] != ")":
    width += s[w_i]
    w_i += 1

  width = int(width)
  
  w_i = s.index("height=") + 7
  while s[w_i] != " " and s[w_i] != ")":
    height += s[w_i]
    w_i += 1

  height = int(height)

  if type == "f":
    w_i = s.index("dx=") + 3
    
    while s[w_i] != " " and s[w_i] != ")":
      dx += s[w_i]
      w_i += 1

    w_i = s.index("dy=") + 3

    while s[w_i] != " " and s[w_i] != ")":
      dy += s[w_i]
      w_i += 1

    dx = int(dx)
    dy = int(dy)
      
  if dx == "":
    dx = 0
    dy = 0

  return type, width, height, dx, dy
  

x = 0
y = 0

lines = file.readlines()
w, h, c = map(int, lines[0].split())
H = h
new_frag = True
i_s = []
D_X = None
D_Y = None

def search_x_y(w_w):
  global x, y, w, H
  k = 0
  while k < len(i_s):
    if (x - w_w <= i_s[k][0]) and ((x > i_s[k][0] and x <= i_s[k][1]) or (x > i_s[k][1])) and y < i_s[k][2]:
      x = i_s[k][1] + w_w
      if x > w: # Слово не помешается в строке
        y += H
        x = w_w
        H = h
        k = -1
    elif x > w:
      y += H
      x = w_w
      H = h
      k = -1
    k += 1

def move_x():
  global x, y
  k = 0
  flag = False
  while k < len(i_s) and flag == False:
   
    if (x-c) <= i_s[k][0] and ((x > i_s[k][0] and x <= i_s[k][1]) or x > i_s[k][1]) and (y < i_s[k][2]):
      x = i_s[k][1]
      
      flag = True
    k += 1
    

img_str = ""

for j in range(1, len(lines)):
  cur = lines[j]
  if cur != "" and cur != "\n" and cur.count(" ") != len(cur):
    i = 0
    
    while i < len(cur):
      if cur[i] != "(" and cur[i] != "\n" and cur[i] != " " and img_str == "":
        # "word " 4
        if new_frag == False:
          x += c # Для пробел перед словом
          if x > w:
            y += H
            x = 0
            H = h
          elif i_s != []:
            move_x()
        else:
          new_frag = False
          
        space = cur.find(" ", i)
        if space == -1:
          space = cur.find("\n", i)
        word = cur[i:space]
      
        x += len(word) * c # Сдвигаем на длину слова
  
        if x > w: # Слово не помешается в строке
          y += H
          x = len(word) * c
          H = h
        
        if i_s != []:
          search_x_y(len(word) * c)
          
        i = space
        D_X = None
        D_Y = None
      elif cur[i] == "(" or img_str != "":
        img_end = cur.find(")", i) + 1
        if img_end == 0:
          img_end = cur.find("\n", i)
          img_str += cur[i:img_end] + " "
          i = img_end
        else:
          img_str += cur[i : img_end]
          type, width, height, dx, dy = ParseImg(img_str)
          i = img_end
          img_str = ""
          if type == "e":
            if new_frag == False: #  Не перывый в фрагменте
              x += c
              if x > w:
                y += H
                x = 0
                H = h
              elif i_s != []:
                move_x()
            else:
              new_frag = False
                  
            x += width
            
            if x > w:
              y += H
              H = h
              x = width

            if i_s != []:
              search_x_y(width)

            res.append(str(x - width) + " " + str(y))
            if H < height:
              H = height # Смена высоты строки
            
          elif type == "s":
            new_frag = True
            x += width
            if x > w:
              y += H
              H = h
              x = width
            if i_s != []:
              search_x_y(width)
            res.append(str(x - width) + " " + str(y))
            i_s.append([x-width, x, y + height])
            i_s.sort(key=lambda x: x[0])
          if type == "f":
            if D_X == None:
              x_f = x + dx
              y_f = y + dy
            else:
              x_f = D_X + dx
              y_f = D_Y + dy
  
            if x_f < 0:
              x_f = 0
            elif x_f + width > w:
              x_f = w - width
            
            res.append(str(x_f) + " " + str(y_f))
            D_X = x_f + width
            D_Y = y_f
          else:
            D_X = None
            D_Y = None        
      
      i += 1

      if i_s != []:
        for k in range(len(i_s), 0):
          if y >= i_s[k][2]:
            del i_s[k]
  else:
    # Новый абзац
    x = 0
    y += H
    H = h
    if i_s != []:
      for k in range(len(i_s)):
        if y < i_s[k][2]:
          y = i_s[k][2]
      i_s = []
    new_frag = True
    D_X = x
    D_Y = y

for i in range(len(res)):
  file1.write(res[i] + "\n")

file1.close
file.close