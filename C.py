file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()

n, m = map(int, lines[0].split())
mas = [int(x) for x in lines[1].split()]

summa = [0] * (n + 1)
    
for i in range(n):
    summa[i+1] = summa[i] + mas[i]

def check(m, params):
    l, s = params
    sum = summa[m + l] - summa[m]
    if sum == s:
        return True
    return sum

def check1(m, params):
    l, s = params
    sum = summa[m + l] - summa[m]
    if sum == s:
        return True
    else:
        return False

def binsearch(l, r, check, params):
    while l < r:
        m = (l + r) // 2
        res = check(m, params)
        if res == True:
            return m
        elif res > s:
            r = m
        else:
            l = m + 1
            
    return l

for i in range(2, m + 2):
    if i != 2:
        file1.write("\n")
    l, s = map(int, lines[i].split())

    if n < l:
        file1.write("-1")
    else:
        res = binsearch(0, n - l, check, [l, s])

        if (check1(res, [l, s]) == True):
            file1.write(str(res + 1))
        else:
            file1.write("-1")

file.close()
file1.close()