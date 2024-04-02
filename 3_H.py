file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()

n = int(lines[0])

a = set()
b = set()

for i in range(1, n + 1):
    x1, y1,x2, y2 = map(int, lines[i].split())
    if (y2 > y1) or (y1 == y2 and x2 < x1):
        x1, y1,x2, y2 = x2, y2, x1, y1
    a.add((x1, y1, x2, y2))

for i in range(n + 1, n * 2 + 1):
    x1, y1,x2, y2 = map(int, lines[i].split())
    if (y2 > y1) or (y1 == y2 and x2 < x1):
        x1, y1,x2, y2 = x2, y2, x1, y1
    b.add((x1, y1, x2, y2))

c = {} # (смещение) : кол-во спичек с таким смещением

for a1 in a:
    for b1 in b:
        if a1[0] - b1[0] == a1[2] - b1[2] and a1[1] - b1[1] == a1[3] - b1[3]:
            sub_x = a1[0] - b1[0]
            sub_y = a1[1] - b1[1]

            if (sub_x, sub_y) not in c:
                c[(sub_x, sub_y)] = 0
            c[(sub_x, sub_y)] += 1

max_ = max(c.values()) if c != {} else 0

file1.write(str(n - max_))

file.close
file1.close