file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()
N = int(lines[0])
count = 0

cols = {}
rows = [0] * N
r = []

def move_col(target):
    c = 0
    for col in cols:
        if col != target:
            c += abs(target - col) * cols[col]
    return c

def move_row():
    global r, rows, count
    j = 0
    for i in range(len(r)):
        num = r[i] - 1
        
        while rows[j] != 0:
            j += 1
        
        rows[j] = 1
        count += abs(num - j)

for i in range(1, N + 1):
    row, col = map(int, lines[i].split())
    
    if col not in cols:
        cols[col] = 0
    cols[col] += 1

   
    if rows[row - 1] == 0:
        rows[row - 1] = 1
    else:
        r.append(row)

r.sort()
move_row()       

middle = N // 2

c = move_col(middle)
flag = True
i = middle-1

while (i != 0) and flag == True:
    c1 = move_col(i) 
    if c1 < c:
        c = c1
    else:
        flag = False
    i -= 1

flag = True
i = middle+1

while (i != N+1) and flag == True:
    c1 = move_col(i) 
    if c1 < c:
        c = c1
    else:
        flag = False
    i += 1

count += c

file1.write(str(count))

file1.close
file.close