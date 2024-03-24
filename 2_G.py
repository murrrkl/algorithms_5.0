file = open('input.txt', 'r')
file1 = open('output.txt', 'w')

lines = file.readlines()
t = int(lines[0])

def cut(a, n):
    res = []
    cur_len = 0
    max_len = 0

    i = 0
    
    while i != n:
        
        if cur_len == 0:
            max_len = a[i]
            cur_len += 1
        elif max_len < cur_len+1 or cur_len + 1 > a[i]: # Больше нет места или a[i] слишком мал
            res.append(cur_len)
            cur_len = 0
            max_len = 0
            i -= 1
        # Максимальная длина на отрезке, больше, чем текущий элемент
        elif max_len > a[i] and cur_len + 1 <= a[i]: # Есть возможность уместить
            max_len = a[i]
            cur_len += 1
        else:
            cur_len += 1
        i += 1
    

    res.append(cur_len)
    file1.write(str(len(res)) + "\n")
    file1.write(str(' '.join(map(str, res))))

for j in range(1, t*2 + 1, 2):
    n = int(lines[j])
    a = [int(x) for x in lines[j+1].split()]
    if j != 1:
        file1.write("\n")
    cut(a, n)

file1.close
file.close