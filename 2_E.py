file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()

N = int(lines[0])

start = []
end = []
height = 0
end_max = []
start_max = []

for i in range(1, N+1):
  a, b  = map(int, lines[i].split())
  
  if (a - b) <= 0:
    if end_max == []:
      end_max = [a, b, i]
    elif end_max[0] < a:
      end_max = [a, b, i] 
    end.append(i)
  else:
    if start_max == []:
      start_max = [a, b, i, a - b]
    elif start_max[3] + a > (a - b) + start_max[0]:
      height += start_max[0] - start_max[1]
      start_max = [a, b, i, a - b]
    else:
      height += a - b
    start.append(i)

if end_max != [] and start_max != []:
    if end_max[0] > start_max[1]:
      height += start_max[3]
      height += end_max[0]
      end.remove(end_max[2])
      start.append(end_max[2])  
    else:
      height += start_max[0]
      start.remove(start_max[2])
      start.append(start_max[2])
elif end_max == []:
  start.remove(start_max[2])
  start.append(start_max[2])
  height += start_max[0]
else:
  height += end_max[0]
  end.remove(end_max[2])
  start.append(end_max[2])

start += end

file1.write(str(height) + "\n")
file1.write(str(' '.join(map(str, start))))

file1.close
file.close