file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()
N = int(lines[0])
K = int(lines[2])

res = []
mas = [int(x) for x in lines[1].split()]
mas.sort()

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l


def min_index(m, params):
    a, L = params
    return a[m] >= L

def max_index(m, params):
    a, R = params
    return a[m] <= R

for i in range(3, K + 3):
    L, R = map(int, lines[i].split()) 
    r = rbinsearch(0, N-1, max_index, [mas, R])
    l = lbinsearch(0, N-1, min_index, [mas, L])

    if l < r or (l == r and max_index(r, [mas, R]) != False and min_index(l, [mas, L]) != False):
        res.append(r - l + 1)
    else:
        res.append(0)

file1.write(" ".join(str(el) for el in res))
file.close
file1.close