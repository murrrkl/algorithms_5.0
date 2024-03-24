file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()

n = int(lines[0])
prize = [int(x) for x in lines[1].split()]
a, b, k = map(int, lines[2].split())

max_prize = 0
v = a
if a % k == 0:
    check_a = ((a // k) - 1) % n
else:
    check_a = (a // k) % n

check = -1

while v <= b and (v == a or (check != check_a)):
    sectors = v // k
    if v % k == 0:
        sectors -= 1
        v = k * (sectors + 1) + k
        check = ((v // k) - 1) % n
    else:
        v = k * sectors + k + 1
        check = (v // k) % n
    
    sectors = sectors % n

    if sectors == 0:
        max_l_r = prize[0]
    else:
        r = prize[sectors]
        l = prize[-1 * (sectors)]
        max_l_r = max(l, r)

    if max_prize < max_l_r:
        max_prize = max_l_r

file1.write(str(max_prize))

file1.close
file.close