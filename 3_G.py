file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

from itertools import combinations

lines = file.readlines()

K = int(lines[0])
points = set()

p3 = ()
p4 = ()
a = 0

two = False
three = False
four = False

for i in range(1, K+1):
    x, y = map(int, lines[i].split())
    points.add((x,y))

i = 0
j = 1

for p1, p2 in combinations(points, 2):
    distance = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
    if four == False and (distance % 2 == 0) or p1[0] == p2[0] or p1[1] == p2[1]:
        sub_x = (p1[0] - p2[0])
        sub_y = (p1[1] - p2[1])

        if sub_x == 0 or sub_y == 0:
            if sub_x == 0:
                p_3 = (p1[0] - abs(sub_y), p1[1])
                p_4 = (p2[0] - abs(sub_y), p2[1])
            else:
                p_3 = (p1[0], p1[1] - abs(sub_x))
                p_4 = (p2[0], p2[1] - abs(sub_x))

            if p_3 in points:
                if p_4 in points:
                    four = True
                elif three == False:
                    three = True
                    p4 = (int(p_4[0]), int(p_4[1]))
            elif three == False and p_4 in points:
                three = True       
                p4 = (int(p_3[0]), int(p_3[1]))
            elif three == False and two == False:
                two = True
                p3 = (int(p_3[0]), int(p_3[1]))
                p4 = (int(p_4[0]), int(p_4[1]))
        
        if four == False and (sub_y % 2 == sub_x % 2):
            x = sub_x / 2
            y = sub_y / 2
            center = (p1[0] - x, p1[1] - y)       
            x, y = y, x

            p_3 = (center[0] + x, center[1] - y)
            x1 = (p1[0] - p_3[0])
            x2 = (p2[0] - p_3[0])
            y1 = (p1[1] - p_3[1])
            y2 = (p2[1] - p_3[1])

            if (abs(x1) == abs(y2) and abs(y1) == abs(x2)):
                p_4 = (center[0] - x, center[1] + y)                
                if p_3 in points:
                    if p_4 in points:
                        four = True
                    elif three == False:
                        three = True
                        p4 = (int(p_4[0]), int(p_4[1]))
                elif three == False and p_4 in points:
                    three = True       
                    p4 = [int(p_3[0]), int(p_3[1])]
                elif three == False and two == False:
                    two = True
                    p3 = (int(p_3[0]), int(p_3[1]))
                    p4 = (int(p_4[0]), int(p_4[1]))              

if four == True:
        file1.write("0")
elif three == True:
    file1.write("1" + "\n")
    file1.write(str(p4[0]) + " " + str(p4[1]))
elif two == True:
    file1.write("2" + "\n")
    file1.write(str(p3[0]) + " " + str(p3[1])+ "\n")
    file1.write(str(p4[0]) + " " + str(p4[1]))
else:
    point = points[0]
    p2 = (point[0] + 1, point[1])
    p3 = (point[0], point[1] - 1)
    p4 = (point[0] + 1, point[1] - 1)
    file1.write("3" + "\n")
    file1.write(str(p2[0]) + " " + str(p2[1])+ "\n")
    file1.write(str(p3[0]) + " " + str(p3[1])+ "\n")
    file1.write(str(p4[0]) + " " + str(p4[1]))       

file.close
file1.close