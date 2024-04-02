n, k = map(int, input().split())
mas = [int(x) for x in input().split()]
dic = {}

i = 0

flag = False

while i != len(mas):
    if mas[i] not in dic:
        dic[mas[i]] = []
    elif i - dic[mas[i]][-1] <= k:
        flag = True 
    dic[mas[i]].append(i)

    i += 1          

if flag == True:
    print("YES")
else:
    print("NO")
