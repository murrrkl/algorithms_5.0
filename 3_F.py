dic = {x for x in input().split()}
text = [x for x in input().split()]
res = []

for t in text:
    i = 0
    while i != len(t) and t[0: i+1] not in dic:
        i += 1
    if i == len(t):
        res.append(t)
    else:
        res.append(t[0: i+1])

print(' '.join(res))