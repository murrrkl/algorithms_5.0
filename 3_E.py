n1 = int(input())
a1 = {int(x) for x in input().split()}

n2 = int(input())
a2 = {int(x) for x in input().split()}

n3 = int(input())
a3 = {int(x) for x in input().split()}

a1_a2 = a1.intersection(a2)
a3_a2 = a3.intersection(a2)
a3_a1 = a3.intersection(a1)

res = a1_a2.union(a3_a2, a3_a1)
res = sorted(res)

if len(res) != 0:
    print(' '.join(map(str, res)))