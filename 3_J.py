n, k = map(int, input().split())

device = {}
device[1] = {}

t = 0

parts = {} # Часть: кол-во скачиваний
requests = {} # к кому: [(часть, от кого)]
device[1] = [set(), {}]

res = [0] * (n - 1)

for i in range(1, k+1):
    parts[i] = 1

for i in range(2, n+1):
    device[i] = [{x for x in range(1, k + 1)}, {}] # номера не скаченных частей ,устройство: кол-во полученных частей

while parts != {}:
    requests = {} # к кому: [(часть, от кого)]
    for d in device:
        if device[d][0] != set(): # Есть не полученные части
            num_part = 0
            count_num_part = n
            # Искомая часть
            for part in device[d][0]:
                if parts[part] < count_num_part or (parts[part] == count_num_part and part < num_part):
                    count_num_part = parts[part]
                    num_part = part
            num_device = 0
            count_parts = 0
            # Запрос к другому устройству

            for d2 in device:
                if num_part not in device[d2][0]:
                    if (num_device == 0) or (count_parts < len(device[d2][0])) or (count_parts == len(device[d2][0]) and d2 < num_device):
                        count_parts = len(device[d2][0])
                        num_device = d2
            if num_device not in requests:
                useful = 0 if d not in device[num_device][1] else device[num_device][1][d]   
                requests[num_device] = (num_part, d, useful)    
            else:
                # Попытка вытолкнуть                
                count_parts = len(device[requests[num_device][1]][0])
                useful_new = 0 if d not in device[num_device][1] else device[num_device][1][d]  
                if (requests[num_device][2] < useful_new) or ((requests[num_device][2] == useful_new) and ((count_parts < len(device[d][0])) or (count_parts == len(device[d][0]) and requests[num_device][1] > d))):
                    requests[num_device] = (num_part, d, useful_new)

    t += 1
    # Отправка частей
    for o in requests:
        device[requests[o][1]][0].remove(requests[o][0])
        if o not in device[requests[o][1]][1]:
            device[requests[o][1]][1][o] = 0
        device[requests[o][1]][1][o] += 1

        if device[requests[o][1]][0] == set():
            res[requests[o][1]-2] = t
        parts[requests[o][0]] += 1
        if parts[requests[o][0]] == n:
            del parts[requests[o][0]]

print(' '.join(str(el) for el in res))