n = int(input())
a = [int(x) for x in input().split()]

dic = {}

for i in range(n):
    c = a[i]
    if c not in dic:
        dic[c] = 0
    dic[c] += 1

max_count = 0

for d in dic:
    cur = dic[d]
    l = 0
    r = 0
    if d - 1 in dic:
        l = dic[d - 1]
    if d + 1 in dic:
        r = dic[d + 1]
    if l > r:
        cur += l
    else:
        cur += r
    if cur > max_count:
        max_count = cur

print(n-max_count)

