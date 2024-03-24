file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()
m, n = map(int, lines[0].split())

res = [[] for i in range(m)]

l_a_1 = []
l_a_2 = []
r_a_1 = []
r_a_2 = []

l_b_1 = []
l_b_2 = []
r_b_1 = []
r_b_2 = []

def color(s, l, r, sym):
    for i in range(l, r+1):
        s[i] = sym
    return s

flag = True
a = False
b = False

i = 0

def set_start_point(row, col):
    return [row, col], [row, col], [row, col], [row, col]

while i != m and flag == True:
    s = list(lines[i + 1])
    if "\n" in s:
        s.remove("\n")
    j = 0
    while j != len(s):   
        if s[j] == "#":
            if a != True and l_a_1 == []: # Фикс левого верхнего края
                l_a_1, l_a_2, r_a_1, r_a_2 = set_start_point(i, j)
            elif a != True and r_a_1[0] == i and r_a_1[1] + 1 == j: # Фикс правого верхнего края
                r_a_1[1] = j
                r_a_2[1] = j
            elif a != True and l_a_2[0] + 1 == i and l_a_2[1] == j: # Фикс левого нижнего края
                l_a_2[0] = i
                r_a_2[0] = i
                r_a_2[1] = j
            elif a != True and r_a_2[0] == i and r_a_2[1] + 1 == j and j <= r_a_1[1] and j >= l_a_1[1]:
                r_a_2[1] = j
            elif a != True and l_a_2[0] + 1 == i and l_a_2[1] > j and l_b_1 == []:
                l_b_1, l_b_2, r_b_1, r_b_2 = set_start_point(i, j)
            elif a != True and r_a_2[0] == i and  r_a_2[1] + 1 != j and l_b_1 == []:
                l_b_1, l_b_2, r_b_1, r_b_2 = set_start_point(i, j)
            elif b != True and l_b_1 == []:
                l_b_1, l_b_2, r_b_1, r_b_2 = set_start_point(i, j)
            elif b != True and r_b_1[0] == i and r_b_1[1] + 1 == j: # Фикс правого верхнего края
                r_b_1[1] = j
                r_b_2[1] = j
            elif b != True and l_b_2[0] + 1 == i and l_b_2[1] == j: # Фикс левого нижнего края
                l_b_2[0] = i
                r_b_2[0] = i
                r_b_2[1] = j
            elif b != True and r_b_2[0] == i and r_b_2[1] + 1 == j and j <= r_b_1[1]:
                r_b_2[1] = j
            elif b != True and a != True and l_b_1[0] == i and r_b_1[0] == i and l_a_2[0] == i and r_b_1[1] < r_a_1[1] and j > r_a_2[1]:
                a = True
                r_b_1[1] = j
                r_b_2[1] = j
                l_a_2[0] -= 1
                r_a_2[0] -= 1
            else:
                flag = False
        else:
            if l_a_1 != [] and l_a_2[0] + 1 == i and j == l_a_2[1]:
                a = True
            elif l_b_1 != [] and l_b_2[0] + 1 == i and j == l_b_2[1]:
                b = True

        j+= 1

    if l_a_1 != [] and l_a_2[0] == i:
        if r_a_2[1] == r_a_1[1]:
            s = color(s, l_a_2[1], r_a_2[1], "a") 
        elif l_b_1 == [] and r_a_2[1] < r_a_1[1]:
            l_b_1 = l_a_2.copy()
            l_b_2 = l_a_2.copy()
            r_b_1 = r_a_2.copy()
            r_b_2 = r_a_2.copy()
            l_a_2[0] -= 1
            r_a_2[0] -= 1
            r_a_2[1] = r_a_1[1]
            a = True
        elif l_b_1 != [] and r_a_2[1] < r_a_1[1] and r_b_1[0] == i:
            r_b_1[1] = r_a_2[1]
            r_b_2[1] = r_a_2[1]
            l_a_2[0] -= 1
            r_a_2[0] -= 1
            r_a_2[1] = r_a_1[1]
            a = True
        else:
            flag = False # Лишний прямоугольник или пересечение
    if l_b_1 != [] and l_b_2[0] == i:
        if r_b_2[1] == r_b_1[1]:
            s = color(s, l_b_2[1], r_b_2[1], "b")
        else:
            flag = False # Лишний прямоугольник или пересечение

    res[i] = s
    i += 1

if flag == True and l_b_1 == []:
    
    if l_a_1 != [] and r_a_1[1] !=  l_a_1[1]:
        sub_vert = ((r_a_1[1] + l_a_1[1]) // 2)
        for i in range(l_a_1[0], l_a_2[0] + 1):
            res[i] = color(res[i], l_a_1[1], sub_vert, "b")
    elif l_a_1 != [] and l_a_2[0] != l_a_1[0]:
        sub_hor = ((l_a_2[0] + l_a_1[0]) // 2)
        for i in range(l_a_1[0], sub_hor + 1):
            res[i] = color(res[i], l_a_1[1], r_a_2[1], "b")
    else:
        flag = False


if flag == True:
    file1.write("YES")
    for i in range(m):
        file1.write("\n" + ''.join(res[i]))
else:
    file1.write("NO")

file.close
file1.close