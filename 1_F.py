# Задача F

file = open('input.txt','r')
file1 = open('output.txt','w')

mult = chr(120)
plus = chr(43)

lines = file.readlines()
n = int(lines[0])
nums = [int(x) for x in lines[1].split()]

signs = [plus] * (n-1)
result = nums[0]
j = 0

for  i in range (1, n):
  result += nums[i]
  if j == 0:
    if ((nums[i] * nums[i-1]) % 2 != 0):
      j = i

if result % 2 == 0:
  signs[j-1] = mult

signs = ''.join(signs)
file1.write(signs)

file.close
file1.close