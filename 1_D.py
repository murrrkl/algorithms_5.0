# Задача D
board = [
  ["*", "*", "*", "*", "*", "*", "*", "*"],
  ["*", "*", "*", "*", "*", "*", "*", "*"],
  ["*", "*", "*", "*", "*", "*", "*", "*"],
  ["*", "*", "*", "*", "*", "*", "*", "*"],
  ["*", "*", "*", "*", "*", "*", "*", "*"],
  ["*", "*", "*", "*", "*", "*", "*", "*"],
  ["*", "*", "*", "*", "*", "*", "*", "*"],
  ["*", "*", "*", "*", "*", "*", "*", "*"]
]

count = 64

def metka1(row, column):
  global board 
  # Верх
  i = row - 1
  while i >= 0 and board[i][column] not in ("R", "B"):
    board[i][column] = "0"
    i -= 1
  # Низ
  i = row + 1
  while i < 8 and board[i][column] not in ("R", "B"):
    board[i][column] = "0"
    i += 1
  # Лево
  j = column - 1
  while j >= 0 and board[row][j] not in ("R", "B"):
    board[row][j] = "0"
    j -= 1
  # Право
  j = column + 1
  while j < 8 and board[row][j] not in ("R", "B"):
    board[row][j] = "0"
    j += 1

def metka2(row, column):
  # Нижняя левая диагональ
  i = row + 1
  j = column - 1
  while i < 8 and j >= 0 and board[i][j] not in ("R", "B"):
    board[i][j] = "0"
    i += 1
    j -= 1

  # Нижняя правая диагональ
  i = row + 1
  j = column + 1

  while i < 8 and j < 8 and board[i][j] not in ("R", "B"):
    board[i][j] = "0"
    i += 1
    j += 1

  # Верхняя левая диагональ
  i = row - 1
  j = column - 1

  while i >= 0 and j >= 0 and board[i][j] not in ("R", "B"):
    board[i][j] = "0"
    i -= 1
    j -= 1

  # Верхняя правая диагональ
  i = row - 1
  j = column + 1

  while i >= 0 and j < 8 and board[i][j] not in ("R", "B"):
    board[i][j] = "0"
    i -= 1
    j += 1

file = open('input.txt','r')
file1 = open('output.txt','w')

lines = file.readlines()

for i in range(8):
  x = lines[i]
  for j in range(8):
    board[i][j] = x[j]

for i in range(8):
  for j in range(8):
    if board[i][j] == "R":
      metka1(i, j)
    elif board[i][j] == "B":
      metka2(i, j)


for i in range(8):
  for j in range(8):
    if board[i][j] in ("0", "R", "B"):
      count -= 1

file1.write(str(count))

for i in range(8):
  print(board[i])

file.close
file1.close