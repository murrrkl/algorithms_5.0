file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()

n, m = map(int, lines[0].split())

n_r = 1
n_c = 1

m_r = 1
m_c = 1

max_n = 0 # Рас
max_m = 0 # Классов

row = [[] for _ in range(n)]

for i in range(1, n + 1): 
  cur = [int(x) for x in lines[i].split()]
  row[i-1] = cur
  for j in range(0, m):
    if cur[j] > max_n:
      max_m = max_n
      m_r = n_r
      m_c = n_c

      max_n = cur[j]
      n_r = i
      n_c = j+1

    elif cur[j] > max_m:  
      max_m = cur[j]
      m_r = i
      m_c = j + 1

if m_r == n_r:
  row[n_r - 1] = [0 for i in range(m)]
  n_col = [row[i][n_c - 1] for i in range(n)]
  m_col = [row[i][m_c - 1] for i in range(n)]

  max_m = 0

  for i in range(n):
    max_in_row = max(row[i])
    if max_m < max_in_row:
      max_m = max_in_row
  

  if (n_c < m_c or max(m_col) != max_m) and max(n_col) == max_m:
    m_c = n_c
  elif max(m_col) != max_m:
    i = 0
    l = 0
    while row[i][j] != max_m and i != n:
      j += 1
      if j == m:
        i += 1
        j = 0
      if i == n_r - 1:
        i += 1
        j = 0
    
    m_c = j + 1

# ищем второй максимум в другом столбце
elif m_c == n_c:
  for i in range(n):
    row[i][n_c - 1] = 0

  max_n = 0

  for i in range(n):
    max_in_row = max(row[i])
    if max_n < max_in_row:
      max_n = max_in_row
    

  if (m_r < n_r or max(row[n_r - 1]) != max_n) and max(row[m_r - 1]) == max_n:
    n_r = m_r
  elif max(row[n_r - 1]) != max_n:
    i = 0
    j = 0
    while i != n and row[i][j] != max_n:
      j += 1
      if j == m:
        i += 1
        j = 0
    
    n_r = i + 1
else:
  n_col = [row[i][n_c - 1] for i in range(n)]
  m_col = [row[i][m_c - 1] for i in range(n)]
  n_col.sort(reverse = True)
  m_col.sort(reverse = True)
  row[n_r - 1].sort(reverse = True)
  row[m_r - 1].sort(reverse = True)

  j = 1
  diff_col = n_col[j]-m_col[j]
  diff_row = row[n_r-1][j] - row[m_r-1][j]

  while j != n and j != m and ((diff_col == 0 and diff_row == 0) or (abs(diff_col) == abs(diff_row))):
    j += 1
    if j != n and j != m:
      diff_col = n_col[j]-m_col[j]
      diff_row = row[n_r-1][j] - row[m_r-1][j]

  if j == n and j != m:
    diff_row = row[n_r-1][j] - row[m_r-1][j]
    while j != m and diff_row == 0:
      j += 1
      if j != m:
        diff_row = row[n_r-1][j] - row[m_r-1][j]
    if j != m and diff_row < 0:
      n_r = m_r
      m_c = n_c
  elif j == m and j != n:
    diff_col = n_col[j]-m_col[j]
    while j != n and diff_col == 0:
      j += 1
      if j != n:
        diff_col = n_col[j]-m_col[j]
    if j != m and diff_col > 0:
      n_r = m_r
      m_c = n_c

  if abs(diff_col) > 0 and abs(diff_row) > 0:

    if diff_col > 0 and diff_row < 0:
      n_r = m_r
      m_c = n_c
    elif (row[n_r-1][j] < n_col[j] or (abs(diff_col) > abs(diff_row))) and diff_col > 0:
      n_r = m_r
      m_c = n_c
    elif (row[m_r-1][j] > m_col[j] or (abs(diff_row) > abs(diff_col))) and diff_row < 0:
      n_r = m_r
      m_c = n_c
    elif diff_row > 0 and diff_col < 0:
      last_r = row[n_r - 1][m-1] - row[m_r - 1][m-1]
      last_c = n_col[n-1] - m_col[n-1]
      
      if (last_r < 0 and (abs(last_r) > diff_row)) or (last_c > 0 and (abs(diff_col) < last_c)):
        n_r = m_r
        m_c = n_c
      else:   
        i = j
        sum_r = 0
        while i != m:
          sum_r += (row[n_r-1][i] - row[m_r-1][i])
          i += 1 

        sum_c = 0
        while j != n:
          sum_c += (n_col[j] - m_col[j])     
          j += 1 

        if sum_r < 0 and abs(sum_r) > diff_row and last_r < 0:
          if (sum_c < 0 and abs(sum_r) > abs(sum_c)) or (sum_c > 0 and sum_c > abs(diff_col) and last_c > 0):        
            n_r = m_r
            m_c = n_c
        elif sum_c > 0 and sum_c > abs(diff_col) and last_c > 0:
          if (sum_r > 0 and sum_c > sum_r): 
            n_r = m_r
            m_c = n_c


  elif abs(diff_col) > 0 and diff_col > 0:
      n_r = m_r
      m_c = n_c
  elif abs(diff_row) > 0 and diff_row < 0:
      n_r = m_r
      m_c = n_c

file1.write(str(n_r) + " " + str(m_c))

file1.close
file.close