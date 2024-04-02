word1 = input()
word2 = input()

dict1 = {}
dict2 = {}

for x in word1:
    if x not in dict1:
        dict1[x] = 0
    dict1[x] += 1

for x in word2:
    if x not in dict2:
        dict2[x] = 0
    dict2[x] += 1

res = all((dict1.get(k) == v for k, v in dict2.items()))

if res == True:
    print("YES")
else:
    print("NO")