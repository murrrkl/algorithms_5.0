file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()
n = int(lines[0])
group = set(x for x in lines[2].split())
count = 0

for i in range(4, 2*n + 1, 2):
    s = set(x for x in lines[i].split())
    group = group.intersection(s)  

group = sorted(group)

file1.write(str(len(group)))

if len(group) != 0:
    file1.write("\n" + group[0])
    for i in range (1, len(group)):
        file1.write(" " + group[i])

file.close
file1.close