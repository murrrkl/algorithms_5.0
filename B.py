n = int(input())

def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l

def search_k(m, n):
    length = int((1 + m) / 2 * m * m) - (m*(m+1)*(m-1))//3
    space = (1 + m) * m // 2 - 1
    length += space
    return length <= n

def check(m, n):
    length = sum(i * (m - (i - 1)) for i in range(1, m + 1))
    space = (1 + m) * m // 2 - 1
    length += space
    return length <= n

k = rbinsearch(0, n, search_k, n)
if (check(k, n) == False):
    k -= 1
print(k)